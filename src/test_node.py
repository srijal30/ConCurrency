from model.crypto import create_keys, serialize_public_key
from model.proto.schema_pb2 import *
from node import *

if __name__ == "__main__":
    test_node = MiningNode(serialize_public_key(create_keys()[1]), int(sys.argv[1]), int(sys.argv[2]))
    test_node.start()        