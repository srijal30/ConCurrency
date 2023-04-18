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


from networking import *
from mining import MiningService


# TO DO: add a way to choose whether to start or join the network and load old data from file
class MiningNode():
    """Implementation of a mining node"""
    
    def __init__(self, pub_key: str):
        self.miner_pub_key: str = pub_key

        # give an option to load all the data later (for now create new)
        model: TalkingStick = TalkingStick()
        # genesis test
        test_block = Block(
                curr_hash="1"*64,
                prev_hash="0"*64,
                miner_pub_key="Satoshi Nakamoto"  
        )
        model.blockchain.blocks.append(test_block)
        print(model.blockchain)
        # we have to make miner check if it is mining the right block
        self.miner = MiningService(self.miner_pub_key, model)  # this might be renamed
        self.server = Network(model)

    def start(self) -> None:
        """Starts the mining node."""
        # testing
        self.miner.mine_next_block(self.miner.callback)
        pass

    def stop(self) -> None:
        """Stop the mining node."""
        pass

    def block_mined(self, block: Block) -> None:
        print(f"{block.miner_pub_key} has mined a block:")
        print(block, "\n\n")




if __name__ == "__main__":
    """
    - Seperate network service into client and server service 
        - Client
            - 
        - Server

        
    checkmarkkkkeddd - Rewrite mining service to work independantly
        -  Make mining service take in DataModel and directly modify
        -
         

    checkmarkedddddddd - Lock Wrappers
        - TalkingStick (threading.Lock)
            - Blockchain
            - Uncommited Snapshot
            - Commited Snapshot
            - Mining Pool

            
    - Create the Network
        -
        -
    
    """
    node = MiningNode()
    node.start()