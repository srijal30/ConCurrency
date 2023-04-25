import sys
sys.path.append("src/model/proto/")

from model.crypto import create_keys, serialize_public_key
from model.proto.schema_pb2 import *
from node import *
from threading import Thread

##generate keys in ../my keys/ please!
#with open('../my keys/public_key.pem', 'rb') as f:
#    v = f.read()
#public_key : str = v
if __name__ == "__main__":
    node0 = MiningNode(serialize_public_key(create_keys()[1]), int(sys.argv[1]), int(sys.argv[2]))
    #node1 = MiningNode(serialize_public_key(create_keys()[1]), 50002, 50001)
    request = GetBlockRequest(
            hash="1"*64
        )
    node0.start()
    #print(node1.client.get_block(request))
    #exit()
    #thread0 = Thread(target = node0.start)
    #thread1 = Thread(target = node1.start)
    #thread0.start()
    #print("thread 0 started")
    #thread1.start()
    #print("thread 1 started")
        