"""
File where all the blockchain data model functionality will be stored
"""

from proto.schema_pb2 import Transaction, Block, BlockChain, Snapshot
from crypto import hash_block, hash_transaction, validate_signature, load_public_key


### BLOCK
def validate_block(committed_snapshot: Snapshot, block: Block, chain: BlockChain) -> bool:
    """Validates block hash correctness and transaction validity. Assumes commited_snapshot is valid."""
    if calculate_difficulty(chain) != block.difficulty:
        return False
    if calculate_reward(chain) != block.reward:
        return False
    if block.curr_hash != hash_block(block) or block.curr_hash[0:block.difficulty] != "0"*block.difficulty:
        return False
    added_transactions = []
    for tran in block.trans:
        added_transactions.append(tran)
        # check if transaction is valid and amount is valid
        if not validate_transaction(tran) or not replay_transaction(committed_snapshot, tran):
            # revert
            for added_tran in reversed(added_transactions):
                undo_transaction(committed_snapshot, added_tran)
            # return false
            return False
    return True

# SEEMS USELESS
# def add_transaction(block: Block, transact: Transaction) -> bool:
#     """Adds transaction to the block if valid. Also updates hash. Returns true if transaction is successfully added."""
#     if not validate_transaction(transact):
#         return False
#     block.trans.append(transact)
#     block.curr_hash = hash_block(block)
#     return True


### TRANSACTION
def validate_transaction(tran: Transaction) -> bool:
    """Validates a transaction's signature and hash."""
    # validate the hash
    if not tran.hash == hash_transaction(tran):
        return False
    # validate the signature
    if not validate_signature(tran.signature, tran.hash, load_public_key(tran.sender_pub_key)):
        return False
    return True


### BLOCKCHAIN
def validate_chain(chain: BlockChain) -> bool:
    # Loop through blockchain array and validate each block
    cur_snapshot = Snapshot()
    prev_hash = None
    for block in chain.blocks:
        # Check if previos hash matches the hash of the previous block
        if prev_hash is not None and block.prev_hash != prev_hash:
            return False
        # Check if the block is valid
        if not validate_block(cur_snapshot, block, chain):
            return False
        prev_hash = block.curr_hash
    return True
    

def add_block(committed_snapshot: Snapshot, block: Block, chain: BlockChain) -> bool:
    """Adds block to the blockchain if valid. Returns whether operation was success. Also updates the committed snapshot."""    
    # Check block validity
    if not validate_block(committed_snapshot, block, chain):
       return False
    # Update the blockchain with new block
    chain.blocks.append(block)
    return True


def calculate_difficulty(chain: BlockChain) -> int:
    """Calculates the difficulty for the next block."""
    return 4


def calculate_reward(chain: BlockChain) -> int:
    """Calculates the mining reward for the next block"""
    return 100


### SNAPSHOT
def replay_transaction(snapshot: Snapshot, tran: Transaction) ->  bool:
    """Checks if sequence number is correct, and that the exchange of coins is valid. Returns true if transaction added to Snapshot successfully."""
    # check if sequence is correct
    if tran.sequence != snapshot.accounts[tran.sender_pub_key].sequence:
        return False
    # send amount to receiver if sender has enough (and update sequence)
    if snapshot.accounts[tran.sender_pub_key].balance >= tran.amount:
        snapshot.accounts[tran.sender_pub_key].sequence += 1
        snapshot.accounts[tran.receiver_pub_key].balance += tran.amount
        snapshot.accounts[tran.sender_pub_key].balance -= tran.amount
        return True
    else:
        return False


def undo_transaction(snapshot: Snapshot, tran: Transaction) -> None:
    """Undoes the effects of a transaction on snapshot"""
    snapshot.accounts[tran.sender_pub_key].sequence -= 1
    snapshot.accounts[tran.receiver_pub_key].balance -= tran.amount
    snapshot.accounts[tran.sender_pub_key].balance += tran.amount