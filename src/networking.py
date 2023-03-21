"""
File that contains the interface for a mining node
"""

from typing import List
from threading import Thread

from proto.schema_pb2_grpc import MiningNodeServicer
from proto.schema_pb2 import (
    BlockChain,
    Transaction,
    GetBlockRequest,
    Block
)


class MiningNode(MiningNodeServicer):
    """Implementation of a mining node"""
    def __init__(self, blockchain: BlockChain):
        self.blockchain = blockchain
        self.transaction_pool : List[Transaction] = []

        # start mining
        self.miner = MiningService(self.blockchain)
        self.miner.start()

    def send_blockchain(self, request, context):
        return super().send_blockchain(request, context)

    def send_transaction(self, request, context):
        return super().send_transaction(request, context)

    def get_block(self, request, context):
        return super().get_block(request, context)

    def announce_block(self, request, context):
        return super().announce_block(request, context)



# should we configure this to allow concurrent mining
class MiningService():
    """Service that mines blocks in the background."""
    def __init__(self, blockchain: BlockChain):
        self.blockchain = blockchain
        self.current_miner = 0
        pass

    # takes in the block that we want to mine
    def start_mining(self, block: Block):
        """Mines blocks until completion or until stopped."""
        # create mining thread
        pass

    def stop_mining(self):
        """Stops the mining process."""
        pass


if __name__ == "__main__":
    node: MiningNode = MiningNode()
    node.start() # this starts running the node

    # let it mine a few blocks
    # then stop


    node.stop()
    pass