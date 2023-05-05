import os
from model.crypto import create_keys, serialize_public_key
from model.proto.schema_pb2 import *
from node import *

if __name__ == "__main__":
    ip = str(sys.argv[1])
    port1 = int(sys.argv[2])
    port2 = int(sys.argv[3])
    pub_key = serialize_public_key(create_keys()[1])

    test_node = MiningNode(pub_key, ip, port1, port2)
    test_node.start()