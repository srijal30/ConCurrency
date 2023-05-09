"""
File that contains the interface for the Node (miner).
"""

import sys
sys.path.append("src/model/proto/")

import grpc
from mining import MiningService
import concurrent.futures as futures

import os
from networking import *
from model.crypto import *
from model.blockchain import TalkingStick
from model.proto.schema_pb2 import *
from model.proto.schema_pb2_grpc import add_NetworkServicer_to_server, NetworkStub
from model.loader import store_blockchain, store_snapshot
import requests
import json
from typing import List

PORT : str = ":5000"
MINER_PORT: str = ":50001"
REND_SERVER : str = "http://192.168.1.178:5000"
# TO DO: add a way to choose whether to start or join the network and load old data from file
class MiningNode():
    """Implementation of a mining node"""
    # the server_port and client_port is temprorary means to an end
    def __init__(self, pub_key: str):
        self.miner_pub_key: str = pub_key

        create_new = True
        if os.path.exists("blockchain.data") and os.path.exists("committed_snapshot.data"):
             create_new = False
        self.model: TalkingStick = TalkingStick(create_new=create_new)
        
        # setup miner
        self.miner = MiningService(self.miner_pub_key, self.model)

        # server setup
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        service = Network(self.model, self.new_block_callback)
        add_NetworkServicer_to_server(service, self.server)
        self.server.add_insecure_port('localhost'+str(MINER_PORT))
        requests.get(REND_SERVER + "/api/connect")

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
        # add the block
        if self.model.add_block(cb_block):
            store_blockchain(self.model.blockchain, 'blockchain.data')
            store_snapshot(self.model.committed_snapshot, "committed_snapshot.data")
        # this is where the block forwarding will go
        #if is_port_in_use(PORT) and self_mined:
        #    request = AnnounceBlockRequest(block= cb_block)
        #    announcer = NetworkStub(channel = grpc.insecure_channel(REND_SERVER+PORT))
        #    announce_block(request)


    # NOTE: has to be updated we implement multiple clients
    def reconcile(self):
        """Gets the current node up to speed with the rest of the network."""
        our_len = len(self.model.blockchain.blocks)
        ip_list : List[str] = json.loads(requests.get(REND_SERVER + "/api/get_nodes").text)
        for x in ip_list:
            try:
                #print(x+MINER_PORT)
                requester = NetworkStub(channel = grpc.insecure_channel(x+MINER_PORT))
                requester.get_chain(GetChainRequest(ip=x))
            except grpc.RpcError as e:
                print(e.details())
            print(x)


        #net_len = self.client.get_chain_length(GetChainLengthRequest()).length
        # if our_len < net_len:
        #     print("DETECTED OLD VERSION OF CHAIN...\n")
        #     updated_chain: GetChainReply = self.client.get_chain(GetChainRequest())
        #     while our_len != net_len:  # this doesnt work if the chains diverge
        #         new_block: GetBlockReply = self.client.get_block(GetBlockRequest(hash=updated_chain.hashes[our_len]))
        #         self.model.add_block(new_block.block)
        #         our_len += 1
        #     store_blockchain(self.model.blockchain, 'blockchain.data')
        #     store_snapshot(self.model.committed_snapshot, "committed_snapshot.data")
        #     print("DONE UPDATING BLOCKCHAIN!")