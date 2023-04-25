"""
File that contains the interface for the Node (miner).

Should combine these modules together
- mining.py
- networking.py
"""

import sys
sys.path.append("src/model/proto/")

from model.crypto import *
from model.blockchain import TalkingStick
from model.proto.schema_pb2 import *
import grpc
import concurrent.futures as futures


from model.proto.schema_pb2_grpc import add_NetworkServicer_to_server, NetworkStub
from networking import *
from mining import MiningService
from threading import get_ident

# TO DO: add a way to choose whether to start or join the network and load old data from file
class MiningNode():
    """Implementation of a mining node"""
    
    def __init__(self, pub_key: str, server_port:int, client_port:int):
        self.miner_pub_key: str = pub_key

        # give an option to load all the data later (for now create new)
        self.model: TalkingStick = TalkingStick()
        # genesis test
        test_block = Block(
                curr_hash="1"*64,
                prev_hash="0"*64,
                miner_pub_key="Satoshi Nakamoto"  
        )
        self.model.blockchain.blocks.append(test_block)
        #print(self.model.blockchain)
        
        # we have to make miner check if it is mining the right block
        self.miner = MiningService(self.miner_pub_key, self.model)  # this might be renamed
        # server channel
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        service = Network(self.model)
        add_NetworkServicer_to_server(service, self.server)
        self.server.add_insecure_port('localhost:'+str(server_port))
        #Client channel
        channel = grpc.insecure_channel('localhost:'+str(client_port))
        self.client = NetworkStub(channel)

    def start(self) -> None:
        """Starts the mining node."""
        # testing
        self.server.start()
        def callback(cb_block : Block) -> None:
            print("thread " + str(get_ident()) + " mined the block")
            print(cb_block)
            request = AnnounceBlockRequest(block= cb_block)
            self.client.announce_block(request)
        self.miner.mine_next_block(callback)
        #server.wait_for_termination()
        pass

    def stop(self) -> None:
        """Stop the mining node."""
        pass

    def block_mined(self, block: Block) -> None:
        print(f"{block.miner_pub_key} has mined a block:")
        print(block, "\n\n")