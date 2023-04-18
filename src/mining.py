"""
File that contains the mining service code.

TO DO:
- make this independent from all other code (except data model)
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
        self.current_thread = Thread(target=self._mine, args=(new_block, callback))
        self.current_thread.start()
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
        block.nonce = 0
        block.curr_hash = hash_block(block)
        while block.curr_hash[0:block.difficulty] != "0"*block.difficulty:
            # stops mining if the prev_hash is no longer valid 
            if not self.model.blockchain.blocks[-1].curr_hash == block.prev_hash:
                return
            block.nonce += 1
            block.curr_hash = hash_block(block)
        callback(block)

    def callback(self, block: Block):
        print("success")
        print(block)
        self.model.blockchain.blocks.append(block)


if __name__ == "__main__":
    pub_key =  "asdasdfasdfasdfasldkf"
    stick = TalkingStick()

    # manually create genesis
    genesis = Block(
        prev_hash="0"*64,
        miner_pub_key="jeff"
    ) 
    genesis.curr_hash = hash_block(genesis)
    stick.blockchain.blocks.append(genesis)

    def callback(block: Block):
        print("successfully mined block")
        print(block)
        if stick.add_block(block):
            # clean up the pool & snapshot (THIS CODE DNRY)
            for tran in block.trans:
                if stick.pool_has(tran.hash):
                    stick.pool_remove(tran.hash)
                else:
                    stick.replay_uncommitted(tran)
            # announce the block (STUB)


    tester = MiningService(pub_key, stick)
    tester.mine_next_block(callback)
    pass