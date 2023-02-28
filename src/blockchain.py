"""
File where all the blockchain data model functionality will be stored
"""

from schema_pb2 import Transaction, Block
from crypto import validate_signature
from crypto import hash_block


def validate_transaction(tran: Transaction) -> bool:
    """Validates a transaction. Returns true or false depending on the result."""
    # validate the signature
    if not validate_signature(tran.signature, tran.sender_pub_key):
        return False
    
    # TO DO: validate the amount
    # ...
    return True


def verify_block(block: Block) -> bool:
    """Verifies block hash correctness and transaction validity"""
    hash_correct : bool = block.curr_hash == hash_block(block)
    for transaction in block.trans:
        if not validate_transaction(transaction):
            return False
    return hash_correct


def add_transaction(block: Block, transact: Transaction):
    """Updates block with new transaction and new hash"""
    if not validate_transaction(transact):
        return 
    block.trans.append(transact)
    block.curr_hash = hash_block(block)



if __name__ == "__main__":    
    pass