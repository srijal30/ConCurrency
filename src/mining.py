"""File where all the mining functions live"""

from schema_pb2 import Transaction, Block, BlockChain, Snapshot, Account
from crypto import validate_signature
from crypto import hash_block
from blockchain import add_block

def mine(block: Block, chain : BlockChain) -> None: 
    "keeps hashing using nonce until successful hash is discovered, and then is added to the blockchain"
    str goal = hash(block)
    while hash(block.nonce) != goal:
        block.nonce = block.nonce + 1

    #at this point the nonce is the correct hash

    add_block(block, chain)
    print("added block")
    return None
