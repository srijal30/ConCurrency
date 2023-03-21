"""
File that contains the interface for a mining node
"""

from threading import Thread
from crypto import hash_block, generate_merkle_root
from blockchain import (
    calculate_difficulty, 
    calculate_reward, 
    replay_transaction, 
    validate_transaction,
    add_block
)
from proto.schema_pb2_grpc import MiningNodeServicer
from proto.schema_pb2 import (
    BlockChain,
    Transaction,
    GetBlockRequest,
    Block,
    Snapshot
)


# TO DO: add a way to choose whether to start or join the network
class MiningNode(MiningNodeServicer):
    """Implementation of a mining node"""
    def __init__(self, miner_pub_key: str):
        self.miner_pub_key = miner_pub_key
        self.transaction_pool = []
        self.miner = MiningService(self)
        
        self.committed_snapshot = Snapshot()
        self.uncommitted_snapshot = Snapshot()
        
        self.blockchain = BlockChain()
        # TEMP: create a genesis block
        # difficulty of genesis block
        genesis = Block(prev_hash="0"*64, merkle_root="0"*64, trans=[])
        genesis.curr_hash = hash_block(genesis)
        add_block(self.committed_snapshot, genesis, self.blockchain)

    def start(self) -> None:
        """Starts the mining node."""
        # join network...
        # start mining
        self.mine_next_block()

    def add_transaction(self, trans : Transaction) -> None:
        """Adds transaction to the pool if it is valid."""
        if validate_transaction(trans) and replay_transaction(self.uncommitted_snapshot, trans):
            self.transaction_pool.append(trans) 

    def mine_next_block(self):
        """Creates and starts mining a new block."""
        # setup the new block
        new_block = Block(
            prev_hash=self.blockchain.blocks[-1].curr_hash,
            trans=self.transaction_pool.copy(),
            miner=self.miner_pub_key,
            difficulty=calculate_difficulty(self.blockchain),
            mining_reward=calculate_reward(self.blockchain),
        )
        generate_merkle_root(new_block)
        self.miner.start_mining(new_block)

    def add_block(self, block: Block):
        """Will get called when new block needs to be added to the chain. 
        Only will add the block after checking validity.
        Will update snapshots and clean up transaction pool."""
        # add the block
        success = add_block(self.committed_snapshot, block, self.blockchain)
        # clean up transactions
        if success:
            for tran in block.trans:
                if tran in self.transaction_pool: # will this code even work? will this compare memory addresses?
                    self.transaction_pool.remove(tran)
                else: # if not in transaction pool, it means we have to add it to uncommited snapshot
                    replay_transaction(self.uncommitted_snapshot, tran)
        # start mining next block
        self.mine_next_block()

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
    def __init__(self, node: MiningNode):
        self.current_thread : Thread = None
        self.stopped = True
        self.parent = node

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