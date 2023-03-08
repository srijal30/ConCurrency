"""Example of a mining app."""

from schema_pb2 import *
from blockchain import *
from crypto import *
from random import sample, randint


DIFFICULTY = 4  # number of zeroes required
USER_COUNT = 10
BLOCK_COUNT = 20


users = [create_keys() for i in range(USER_COUNT)]
transaction_pool = []
snapshot = Snapshot()
chain = BlockChain()
genesis = Block(prev_hash="0"*64, merkle_root="0"*64, trans=[])
genesis.curr_hash = hash_block(genesis)
add_block(snapshot, genesis, chain)


# creates valid transaction randomly
def random_transaction():
    sender, receiver = sample(users, 2)
    
    t = Transaction()
    t.sender_pub_key = serialize_public_key(sender[1])
    t.receiver_pub_key = serialize_public_key(receiver[1])
    t.sequence = snapshot.accounts[t.sender_pub_key].sequence
    
    t.amount = 0
    # t.amount = randint(1, snapshot.accounts[sender_pub])
    
    t.hash = hash_transaction(t)
    t.signature = create_signature(t.hash, sender[0])
    return t        


# mines a block until it reaches desired difficulty
def mine(block: Block) -> None:
    block.nonce = 0
    block.curr_hash = hash_block(block)
    while block.curr_hash[0:DIFFICULTY] != "0"*DIFFICULTY:
        block.nonce += 1
        block.curr_hash = hash_block(block)


# mine 20 blocks
block_cntr = 0
while block_cntr < BLOCK_COUNT:
    #create new block
    block = Block()
    block.prev_hash = chain.blocks[-1].curr_hash
    
    # add 1-5 transactions to the block
    cnt = randint(1, 6)
    for i in range(cnt):
        block.trans.append(random_transaction())

    # generate the merkle root
    generate_merkle_root(block)

    # mine the block (find cur_hash and nonce)
    mine(block)

    # add it to the chain
    add_block(snapshot, block, chain)
    block_cntr += 1
    # print(block_cntr)

    # print block (simulation)
    print(f"BLOCK #{block_cntr}:\n{str(chain.blocks[-1])}\n")
    input("PRESS ENTER")


# print the blockchain
# print(chain)

# check validity
# print(validate_chain(chain))


# mess with the chain's amount
# chain.blocks[10].trans[0].amount = 100
# print(validate_chain(chain))


# check if snapshot is working
# print(snapshot)