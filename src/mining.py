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
    while block.curr_hash[0:block.difficulty] != "0"*block.difficulty: 
        block.nonce += 1
        block.curr_hash = hash_block(block)

###TESTING
DIFFICULTY = 4  # number of zeroes required
USER_COUNT = 10
BLOCK_COUNT = 1


snapshot = Snapshot()


chain = BlockChain()
genesis = Block(prev_hash="0"*64, merkle_root="0"*64, trans=[])
genesis.curr_hash = hash_block(genesis)
add_block(snapshot, genesis, chain)
print("genesis done\n\n")

users = [create_keys() for i in range(USER_COUNT)]
transaction_pool : List[Transaction]= []
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

commit_snapshot = Snapshot()
# mine 20 blocks
block_cntr = 0
while block_cntr < BLOCK_COUNT:
    #create new block
    block = Block()
    block.prev_hash = chain.blocks[-1].curr_hash

    # committed
    uncommitted_snapshot = Snapshot()

    transList : List[Transaction] = []

    # add 1-5 transactions to the block
    # cnt = 1
    # for i in range(cnt):
    #     randomtrans = random_transaction()
    #     play_transaction(uncommitted_snapshot, randomtrans)
    #     block.trans.append(randomtrans)

    commit_snapshot = uncommitted_snapshot
    ## generate the merkle root
    generate_merkle_root(block)
    #print(str(block.trans))
    # mine the block (find cur_hash and nonce)
    mine(block)

    # add it to the chain
    add_block(commit_snapshot, block, chain)
    #input()
    #block_cntr += 1
    ## print(block_cntr)
    # #print(f"BLOCK #{block_cntr}:\n{str(chain.blocks[-1])}\n")
    ## print block (simulation)
    # #input("PRESS ENTER")

print(snapshot)
