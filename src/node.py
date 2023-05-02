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

# TO DO: add a way to choose whether to start or join the network and load old data from file
class MiningNode():
    """Implementation of a mining node"""
    # the server_port and client_port is temprorary means to an end
    def __init__(self, pub_key: str, server_port:int, client_port:int):
        self.miner_pub_key: str = pub_key
        self.client_port: int = client_port
        self.server_port: int = server_port

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
        self.server.add_insecure_port('localhost:'+str(server_port))
        
        # client(s) setup
        channel = grpc.insecure_channel('localhost:'+str(client_port))
        self.client = NetworkStub(channel)


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
            if is_port_in_use(self.client_port) and self_mined:
                request = AnnounceBlockRequest(block= cb_block)
                self.client.announce_block(request)