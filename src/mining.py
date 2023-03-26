"""
File that contains the mining service code.

TO DO:
- make this independent from all other code (except data model)

"""

from proto.schema_pb2 import *
from crypto import *
from threading import Thread

# TO DO: purge all code that relies on the existence of `parent` or `node` 
class MiningService():
    """Service that mines blocks in the background."""
    def __init__(self, node):
        self.current_thread : Thread = None
        self.stopped = True
        self.parent = node

    def _mine(self, block: Block) -> None: 
        """Mines blocks until signed hash is generated."""
        block.nonce = 0
        block.curr_hash = hash_block(block)
        while block.curr_hash[0:block.difficulty] != "0"*block.difficulty:
            #print(block.nonce)
            if self.stopped:  # stops without calling callback
                return
            block.nonce += 1
            block.curr_hash = hash_block(block)
        # since fully completes, callback can be called
        print("successfully mined block")
        # print(len(self.parent.blockchain.blocks))
        self.parent.add_block(block)

    def start_mining(self, block: Block) -> None:
        """Creates thread for mining"""
        self.stopped = False
        self.current_thread = Thread(target=self._mine, args=(block,))
        self.current_thread.start()

    def stop_mining(self):
        """Stops the mining process."""
        self.stopped = True
        self.current_thread.join()  # blocks until thread joins back