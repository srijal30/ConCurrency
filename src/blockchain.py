"""
File where all the blockchain data model functionality will be stored
"""

from proto.schema_pb2 import Transaction, Block, BlockChain, Snapshot
from crypto import hash_block, hash_transaction, validate_signature, load_public_key
from time import time


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


def calculate_difficulty(blockchain : BlockChain, block_index : int, blocks_to_recalculate_difficulty=2016):
    # Recalculate difficulty every n blocks
    if block_index % blocks_to_recalculate_difficulty == 0 and block_index > 0:
        # Get the time it took to mine the previous n blocks
        prev_time = (blockchain[block_index-1]['timestamp'] - blockchain[block_index-blocks_to_recalculate_difficulty]['timestamp']) / 1000
        # Calculate the ideal time it should have taken to mine n blocks
        ideal_time = blocks_to_recalculate_difficulty * 10 * 60  # 10 minutes per block
        # Adjust difficulty based on the ratio of actual time to ideal time
        ratio = prev_time / ideal_time
        if ratio > 1:
            # Difficulty should be decreased to make mining easier
            difficulty = int(blockchain[block_index-1]['difficulty'] / ratio)
        else:
            # Difficulty should be increased to make mining harder
            difficulty = int(blockchain[block_index-1]['difficulty'] * ratio)
    else:
        # Use the previous block's difficulty if not recalculating difficulty
        difficulty = blockchain[block_index-1]['difficulty']
    return difficulty


### no clue if this works at all
def calculate_reward(chain: BlockChain) -> int:
    """Calculates the mining reward for the next block"""
    last_block = chain.blocks[-1]
    last_reward = last_block.mining_reward
    last_timestamp = last_block.timestamp
    last_difficulty = calculate_difficulty(chain, len(chain.blocks) - 1)  # Use updated difficulty
    time_since_last_block = time.time() - last_timestamp
    max_reward = 10  # maximum reward per block
    halving_interval = 500  # number of blocks after which reward is halved
    block_count = len(chain.blocks)
    
    if block_count >= halving_interval:
        halvings = block_count // halving_interval
        reward = max_reward / 2**halvings
        if reward < 1:
            reward = 1
    else:
        reward = max_reward
    
    total_reward = reward + sum(tran.fee for tran in last_block.trans)  # add transaction fees
    if time_since_last_block < 60:
        return total_reward
    else:
        return total_reward * (1 + last_difficulty) * (time_since_last_block // 60)

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