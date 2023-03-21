"""
File with all the networking functionality
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



class MiningService():
    """Service that mines blocks in the background"""
    def __init__(self, blockchain: BlockChain):
        self.blockchain = blockchain

        # create a thread for mining
        pass

    def mine(self, block: Block):
        """Mines blocks until completion or until stopped."""
        # create mining thread
        pass



if __name__ == "__main__":
    pass