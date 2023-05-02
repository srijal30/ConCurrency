"""
File that contains the interface for the Node (miner).

Should combine these modules together
- mining.py
- networking.py
"""

import sys
sys.path.append("src/model/proto/")

import grpc
import concurrent.futures as futures
from model.crypto import *
from model.blockchain import TalkingStick
from model.proto.schema_pb2 import *
from model.proto.schema_pb2_grpc import add_NetworkServicer_to_server, NetworkStub
from model.loader import store_blockchain, store_block
from networking import *
from mining import MiningService

# TO DO: add a way to choose whether to start or join the network and load old data from file
class MiningNode():
    """Implementation of a mining node"""
    # the server_port and client_port is temprorary means to an end
    def __init__(self, pub_key: str, server_port:int, client_port:int):
        self.miner_pub_key: str = pub_key
        self.client_port: int = client_port
        self.server_port: int = server_port

        # give an option to load all the data later (for now create new chain)
        self.model: TalkingStick = TalkingStick()
        # genesis block
        genesis = Block(
                curr_hash="1"*64,
                prev_hash="0"*64,
                miner_pub_key="Satoshi Nakamoto"  
        )
        self.model.blockchain.blocks.append(genesis)
        
        # setup miner
        self.miner = MiningService(self.miner_pub_key, self.model)

        # server setup
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        service = Network(self.model)
        add_NetworkServicer_to_server(service, self.server)
        self.server.add_insecure_port('localhost:'+str(server_port))
        
        # client(s) setup
        channel = grpc.insecure_channel('localhost:'+str(client_port))
        self.client = NetworkStub(channel)

    def start(self) -> None:
        """Starts the mining node."""
        # start server
        self.server.start()
        # start mining
        self.miner.start(self.callback)
        # server.wait_for_termination() # we dont need this?

    def stop(self) -> None:
        """Stop the mining node."""
        pass

    def callback(self, cb_block: Block) -> None:
            """callback for the mining node"""
            self.model.add_block(cb_block)
            store_blockchain(self.model.blockchain, 'blockchain.data')
            if is_port_in_use(self.client_port):
                request = AnnounceBlockRequest(block= cb_block)
                self.client.announce_block(request)