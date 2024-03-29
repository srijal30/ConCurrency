"""
File that contains the interface for the Node (miner).
"""

import sys
sys.path.append("src/model/proto/")

import os
import grpc
import json
import requests
from typing import List
from random import choice
import concurrent.futures as futures
from time import time

from mining import MiningService
from networking import *
from model.crypto import *
from model.blockchain import TalkingStick
from model.proto.schema_pb2 import *
from model.proto.schema_pb2_grpc import add_NetworkServicer_to_server, NetworkStub
from model.proto.server_pb2 import *
from model.proto.server_pb2_grpc import add_ServerServicer_to_server
from model.loader import store_blockchain, store_snapshot

MINER_PORT: str = ":50001"

REND_SERVER : str = "http://marge.stuy.edu:5000"
REND_SERVER_RESPONSE_SERVER_PORT = ":50002"

# TO DO: add a way to choose whether to start or join the network and load old data from file
class MiningNode():
    """Implementation of a mining node"""
    # the server_port and client_port is temprorary means to an end
    def __init__(self, pub_key: str):
        self.miner_pub_key: str = pub_key

        #NOTE: fix this
        create_new = True
        if os.path.exists("blockchain.data") and os.path.exists("committed_snapshot.data"):
             create_new = False
        self.model: TalkingStick = TalkingStick(create_new=create_new)
        
        # setup miner
        self.miner = MiningService(self.miner_pub_key, self.model)

        # node server setup
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        service = Network(self.model, self.new_block_callback)
        add_NetworkServicer_to_server(service, self.server)
        self.server.add_insecure_port('0.0.0.0'+MINER_PORT)

        # rend_server response server setup

        # reconcile the node with the network
        self.reconcile()

    def start(self) -> None:
        """Starts the mining node."""
        self.server.start()
        self.miner.start(self.new_block_callback)
        

    def stop(self) -> None:
        """Stop the mining node."""
        pass

    # for now it takes an extra argument, but later we can just forward block in both cases
    def new_block_callback(self, cb_block: Block, self_mined: bool) -> None:
        """Callback for when a new block needs to be added to the chain."""
        # logging
        print(("MINED" if self_mined else "RECEIVED") + " A NEW BLOCK\n", cb_block, "\n", sep="")
        print(("/nMINED AT: " + str(time())))
        # add the block
        if self.model.add_block(cb_block):
            store_blockchain(self.model.blockchain, 'blockchain.data')
            store_snapshot(self.model.committed_snapshot, "committed_snapshot.data")
        # this is where the block forwarding will go
        for ip in self.get_ip_list():
            request = AnnounceBlockRequest(block= cb_block)
            announcer = NetworkStub(channel = grpc.insecure_channel(ip+MINER_PORT))
            announcer.announce_block(request)

    def get_ip_list(self):
        """Get the ips from Rend Server"""
        self.rend_server.get_ips()
        ip_list : List[str] = json.loads(requests.get(REND_SERVER + "/api/get_nodes").text)
        if self.ip in ip_list:
            ip_list.remove(self.ip)
        return ip_list

    # NOTE: has to be updated we implement multiple clients
    def reconcile(self):
        """Gets the current node up to speed with the rest of the network."""
        # choose a random node to connect to
        ip_list = self.get_ip_list()
        if len(ip_list) < 1:
            return
        ip = choice(ip_list)
        channel = grpc.insecure_channel(ip+MINER_PORT)
        client = NetworkStub(channel)

        net_len = client.get_chain_length(GetChainLengthRequest()).length
        our_len = len(self.model.blockchain.blocks)

        if our_len < net_len:
            print("DETECTED OLD VERSION OF CHAIN...\n")
            updated_chain: GetChainReply = client.get_chain(GetChainRequest())
            while our_len != net_len:  # this doesnt work if the chains diverge
                new_block: GetBlockReply = client.get_block(GetBlockRequest(hash=updated_chain.hashes[our_len]))
                self.model.add_block(new_block.block)
                our_len += 1
            store_blockchain(self.model.blockchain, 'blockchain.data')
            store_snapshot(self.model.committed_snapshot, "committed_snapshot.data")
            print("DONE UPDATING BLOCKCHAIN!")

if __name__ == "__main__":
    pub_key = serialize_public_key(create_keys()[1])
    test_node = MiningNode(pub_key)
    test_node.start_node()
