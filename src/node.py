"""
File that contains the interface for the Node (miner).

Should combine these modules together
- mining.py
- networking.py
"""

from crypto import hash_block, generate_merkle_root
from blockchain import (
    calculate_difficulty, 
    calculate_reward, 
    replay_transaction, 
    validate_transaction,
    add_block,
    validate_chain
)
from proto.schema_pb2_grpc import MiningNodeServicer
from proto.schema_pb2 import (
    BlockChain,
    Transaction,
    GetBlockRequest,
    Block,
    Snapshot
)
from mining import MiningService


# TO DO: rewrite this entire class
# TO DO: add a way to choose whether to start or join the network and load old data from file
class MiningNode(MiningNodeServicer):
    """Implementation of a mining node"""
    def __init__(self, miner_pub_key: str):
        self.miner_pub_key = miner_pub_key
        self.transaction_pool = []
        self.stopped = True
        self.miner = MiningService(self)
        
        self.committed_snapshot = Snapshot()
        self.uncommitted_snapshot = Snapshot()
        
        self.blockchain = BlockChain()
        # TEMP: create a genesis block
        # difficulty of genesis block
        genesis = Block(prev_hash="0"*64, merkle_root="0"*64, trans=[])
        genesis.curr_hash = hash_block(genesis)
        add_block(self.committed_snapshot, genesis, self.blockchain)

    def stop(self) -> None:
        """Stop the mining node."""
        self.stopped = True

    def start(self) -> None:
        """Starts the mining node."""
        # join network...
        # start mining
        self.stopped = False
        self.mine_next_block()

    def add_transaction(self, trans : Transaction) -> None:
        """Adds transaction to the pool if it is valid."""
        if validate_transaction(trans) and replay_transaction(self.uncommitted_snapshot, trans):
            self.transaction_pool.append(trans) 

    def mine_next_block(self):
        """Creates and starts mining a new block."""
        if len(self.transaction_pool) > 10:
            transactions_to_be_mined : list = self.transaction_pool[0:10]
        else:
            transactions_to_be_mined : list = self.transaction_pool[0:]
        # setup the new block
        new_block = Block(
            prev_hash=self.blockchain.blocks[-1].curr_hash, 
            trans=transactions_to_be_mined,
            miner=self.miner_pub_key,
            difficulty=calculate_difficulty(self.blockchain),
            mining_reward=calculate_reward(self.blockchain),
        )
        generate_merkle_root(new_block)
        if not self.stopped:
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
        
        # print("done mining", len(self.blockchain.blocks), validate_chain(self.blockchain), block.curr_hash)  # DEBUG
        self.mine_next_block()