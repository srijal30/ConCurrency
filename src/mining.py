"""
File that contains the mining service code.

TO DO:
- make this independent from all other code (except data model)
"""

from proto.schema_pb2 import *
from crypto import *
from threading import Thread

class MiningService():
    """Service that mines blocks in the background."""
    def __init__(self):
        self.current_thread : Thread = None
        self.stopped = True

    # TO DO: what should we do when we finish mining?
    def _mine(self, block: Block) -> None: 
        """Mines blocks until signed hash is generated."""
        block.nonce = 0
        block.curr_hash = hash_block(block)
        while block.curr_hash[0:block.difficulty] != "0"*block.difficulty:
            if self.stopped:  # stops without calling callback
                return
            block.nonce += 1
            block.curr_hash = hash_block(block)
        # since fully completes, callback can be called
        print("successfully mined block, callback not implemented...")

    def start_mining(self, block: Block) -> None:
        """Creates thread for mining"""
        self.stopped = False
        self.current_thread = Thread(target=self._mine, args=(block,))
        self.current_thread.start()

    def stop_mining(self):
        """Stops the mining process."""
        self.stopped = True
        self.current_thread.join()  # blocks until thread joins back