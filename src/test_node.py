import os
from model.crypto import create_keys, serialize_public_key
from model.proto.schema_pb2 import *
from node import *

if __name__ == "__main__":
    pub_key = serialize_public_key(create_keys()[1])

    test_node = MiningNode(pub_key)
    test_node.start()
