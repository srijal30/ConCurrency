"""Example of a mining app."""

from proto.schema_pb2 import *
from blockchain import *
from crypto import *
from random import sample, randint

# mines a block until it reaches desired difficulty
def mine(block: Block) -> None:
    """Mines block until correct number of 0s is reached."""
    block.nonce = 0
    block.curr_hash = hash_block(block)
    while block.curr_hash[0:DIFFICULTY] != "0"*DIFFICULTY:
        block.nonce += 1
        block.curr_hash = hash_block(block)


###TESTING
DIFFICULTY = 4  # number of zeroes required
USER_COUNT = 10
BLOCK_COUNT = 1
REWARD = 100 #amount of coin rewarded per successful hash


miner_priv, miner_pub = create_keys()
print("THE MINER IS:", serialize_public_key(miner_pub))
users = [create_keys() for i in range(USER_COUNT)]
transaction_pool = []

# committed
snapshot = Snapshot()




chain = BlockChain()
genesis = Block(prev_hash="0"*64, merkle_root="0"*64, trans=[])
genesis.curr_hash = hash_block(genesis)
add_block(snapshot, genesis, chain)
print("genesis done\n\n")

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


# mine 20 blocks
block_cntr = 0
while block_cntr < BLOCK_COUNT:
    #create new block
    block = Block()
    block.prev_hash = chain.blocks[-1].curr_hash
    # uncommited                        
    uncommitted_snapshot = Snapshot()   # add 1-5 transactions to the block
    cnt = 0
    for i in range(cnt):
        randomtrans = random_transaction()
        validate_transaction(random_transaction)
        replay_transaction(uncommitted_snapshot, randomtrans)


    # add reward
    #block.trans.append(Transaction(
    #    sender_pub_key = MINTING_PUB,
    #    receiver_pub_key = serialize_public_key(miner_pub),
    #    amount = REWARD,
    #    sequence = snapshot.accounts[MINTING_PUB].sequence
    #))
    #block.trans[-1].hash = hash_transaction(block.trans[-1])
    #block.trans[-1].signature = create_signature(block.trans[-1].hash, load_private_key(MINTING_PRIV))

    ## generate the merkle root
    #generate_merkle_root(block)

    # mine the block (find cur_hash and nonce)
    mine(block)

    # add it to the chain
    print("SUCCESS:",  add_block(snapshot, block, chain))
    input()
    block_cntr += 1
    # print(block_cntr)
    print(f"BLOCK #{block_cntr}:\n{str(chain.blocks[-1])}\n")

    # print block (simulation)
    input("PRESS ENTER")


# print the blockchain
# print(chain)

# check validity
# print(validate_chain(chain))


# mess with the chain's amount
# chain.blocks[10].trans[0].amount = 100
# print(validate_chain(chain))

# check if snapshot is working
print(snapshot)
