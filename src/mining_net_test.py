from threading import Thread
from time import sleep
from random import randint, sample

from networking import *
from blockchain import *
from proto.schema_pb2 import *
from crypto import *


print("genesis done\n\n")   
users = [create_keys() for i in range(10)]

def random_transaction(node):
    sender, receiver = sample(users, 2)
    t = Transaction()
    t.sender_pub_key = serialize_public_key(sender[1])
    t.receiver_pub_key = serialize_public_key(receiver[1])
    t.sequence = node.snapshot.accounts[t.sender_pub_key].sequence
    t.amount = 0
    # t.amount = randint(1, snapshot.accounts[sender_pub])
    t.hash = hash_transaction(t)
    t.signature = create_signature(t.hash, sender[0])
    return t        



def give_transactions(node: MiningNode):
    sleep(1)
    node.add_transaction(random_transaction(node))


# START
test = MiningNode()
test.start()

# adds transactions every second
tran_sender= Thread(target=give_transactions, args=(test,))
tran_sender.start()

STOP_AT = 2
while len(test.blockchain.blocks) != STOP_AT:
    pass
test.stop()

