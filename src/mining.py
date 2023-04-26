"""
File that contains the mining service code.

TO DO:
- make this independent from all other code (except data model)
- MAX_TRANSACTIONS constnat should be moved somewhere else
"""

from typing import Callable
from model.proto.schema_pb2 import *
from model.crypto import *
from model.blockchain import TalkingStick


from threading import Thread

# add a way for it to stop
class MiningService():
    """Service that mines blocks."""
    def __init__(self, pub_key: str, stick: TalkingStick):
        self.miner_pub_key = pub_key
        self.model = stick
        self.current_thread: Thread = None        

    def mine_next_block(self, callback: Callable):
        new_block = self.prepare_next_block()
        print("new block prepared\n")
        self._mine(new_block, callback)
        self.mine_next_block(callback)

    def prepare_next_block(self) -> Block:
        # setup the new block
        new_block = Block(
            prev_hash=self.model.blockchain.blocks[-1].curr_hash, 
            miner_pub_key=self.miner_pub_key,
            difficulty=self.model.calculate_difficulty(),
            reward=self.model.calculate_reward(),
        )
        # add the transactions
        MAX_TRANSACTIONS = 10
        ctr = 0
        for hash, tran in self.model.trans_pool:
            new_block.trans.append(tran)
            ctr += 1
            if ctr == MAX_TRANSACTIONS:
                break
        generate_merkle_root(new_block)
        return new_block

    def _mine(self, block: Block, callback: Callable) -> None: 
        """Mines blocks until signed hash is generated."""
        print("starting mining\n")
        block.nonce = 0
        block.curr_hash = hash_block(block)
        while block.curr_hash[0:block.difficulty] != "0"*block.difficulty:
            # stops mining if the prev_hash is no longer valid 
            if not self.model.blockchain.blocks[-1].curr_hash == block.prev_hash:
                print("someone else finished mining first")
                return
            block.nonce += 1
            block.curr_hash = hash_block(block)
        print("finished mining")
        callback(block)