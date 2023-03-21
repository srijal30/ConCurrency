"""
File that contains the interface for a mining node
"""

from threading import Thread
from crypto import hash_block
from blockchain import calculate_difficulty, calculate_reward, replay_transaction, validate_transaction

from proto.schema_pb2_grpc import MiningNodeServicer
from proto.schema_pb2 import (
    BlockChain,
    Transaction,
    GetBlockRequest,
    Block,
    Snapshot
)

class MiningNode(MiningNodeServicer):
    """Implementation of a mining node"""
    def __init__(self, miner_pub_key: str):
        self.miner_pub_key = miner_pub_key
        self.transaction_pool = []
        
        self.committed_snapshot = Snapshot()
        self.uncommitted_snapshot = Snapshot()
        
        self.blockchain = BlockChain()
        self.genesis = Block(prev_hash="0"*64, merkle_root="0"*64, trans=[])
        self.genesis.curr_hash = hash_block(self.genesis)
        
        self.miner = MiningService(self.mine_next_block)
        
    def add_transaction(self, trans : Transaction) -> None:
        """Adds transactions to pool after verifying and adding to uncommitted snapshot."""
        if validate_transaction(trans) and replay_transaction(self.uncommitted_snapshot, trans):
            self.transaction_pool.append(trans) 

    def mine_next_block(self):
        """Creates a new block to be mined"""
        new_block = Block()
        new_block.trans = self.transaction_pool.copy()
        new_block.miner = self.miner_pub_key
        new_block.difficulty = calculate_difficulty(self.blockchain)
        new_block.mining_reward = calculate_reward(self.blockchain)


    def start(self) -> None:
        """Starts the mining node."""
        # join network
        # start mining
        self.mine_next_block()
        pass

    def mining_finished() -> None:
        """This will be called when the mining service finishes mining a block"""
        pass

    # NETWORKING FUNCTIONS
    def send_blockchain(self, request, context):
        return super().send_blockchain(request, context)

    def send_transaction(self, request, context):
        return super().send_transaction(request, context)

    def get_block(self, request, context):
        return super().get_block(request, context)

    def announce_block(self, request, context):
        return super().announce_block(request, context)


# should we make mining service spawn multiple threads to make mining faster
class MiningService():
    """Service that mines blocks in the background."""
    def __init__(self, callback: function):
        self.current_thread : Thread = None
        self.stopped = True
        self.callback = callback

    def _mine(self, block: Block, difficulty: int) -> None: 
        """Mines blocks until signed hash is generated."""
        block.nonce = 0
        block.curr_hash = hash_block(block)
        while block.curr_hash[0:difficulty] != "0"*difficulty:
            if self.stopped:
                return
            block.nonce += 1
            block.curr_hash = hash_block(block)
        self.callback()

    def start_mining(self, block: Block, difficulty: int) -> None:
        """Creates thread for mining"""
        self.stopped = False
        self.current_thread = Thread(target=self._mine, args=(block, difficulty,))
        self.current_thread.start()

    def stop_mining(self):
        """Stops the mining process."""
        self.stopped = True
        self.current_thread.join()  # blocks until thread joins back