from threading import Thread
from time import sleep
import sys
from random import randint, sample

from networking import *
from blockchain import *
from proto.schema_pb2 import *
from crypto import *


MAX_BLOCKS = 2
users = [create_keys() for i in range(10)]
miner_pub_key = serialize_public_key(create_keys()[1])
print("MINER:", miner_pub_key)


def random_transaction(node: MiningNode):
    sender, receiver = sample(users, 2)
    t = Transaction()
    t.sender_pub_key = serialize_public_key(sender[1])
    t.receiver_pub_key = serialize_public_key(receiver[1])
    t.sequence = node.uncommitted_snapshot.accounts[t.sender_pub_key].sequence
    t.amount = 0
    # t.amount = randint(1, snapshot.accounts[sender_pub])
    t.hash = hash_transaction(t)
    t.signature = create_signature(t.hash, sender[0])
    return t        


def give_transactions(node: MiningNode):
    while len(node.blockchain.blocks) != MAX_BLOCKS:
        sleep(1)
        print("tran added")
        node.add_transaction(random_transaction(node))


# START OF TESTING
test = MiningNode(miner_pub_key)
test.start()

# adds transactions every second
tran_sender= Thread(target=give_transactions, args=(test,))
tran_sender.start()

while len(test.blockchain.blocks) != MAX_BLOCKS:
    print(len(test.blockchain.blocks))
    pass
print(len(test.blockchain.blocks))
print("here1")
test.stop()
tran_sender.join()

print("SNAPSHOT")
print(test.committed_snapshot)
print("\nBLOCKCHAIN")
print(test.blockchain)