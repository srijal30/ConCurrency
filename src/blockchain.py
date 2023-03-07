"""
File where all the blockchain data model functionality will be stored
"""

from schema_pb2 import Transaction, Block, BlockChain, Snapshot, Account
from crypto import validate_signature
from crypto import hash_block


### BLOCK

def validate_block(block: Block) -> bool:
    """Validates block hash correctness and transaction validity"""
    hash_correct : bool = block.curr_hash == hash_block(block)
    for transaction in block.trans:
        if not validate_transaction(transaction):
            return False
    return hash_correct


def add_transaction(block: Block, transact: Transaction) -> bool:
    """Updates block with new transaction and hash (if valid). Returns transaction validity."""
    if not validate_transaction(transact):
        return False
    block.trans.append(transact)
    block.curr_hash = hash_block(block)
    return True


### TRANSACTION

def validate_transaction(tran: Transaction) -> bool:
    """Validates a transaction. Returns true or false depending on the result."""
    # stub
    correct_transaction: bool = tran.hash() == hash(tran.receiver_pub_key, tran.signature, tran.amount, tran.sequence)
    return correct_transaction


### BLOCKCHAIN

def verify_chain(chain: BlockChain) -> bool:
    ### Loop through blockchain array and validate each block
    for block in chain.block:
        if not validate_block(block):
            print("bad block")
            return False
    
    ### At this point chain is valid
    print("validdddd")
    return True

def add_block(block: Block, chain: BlockChain):
    ### Add block to blockchain
    ### One line solution????? wow what is this i am definitely missing something
    chain.block.append(Block)
    return None


### SNAPSHOT

def replay_block(snapshot: Snapshot, block: Block) ->  None:  # what do we return
    pass


### TESTING

if __name__ == "__main__":    
    pass