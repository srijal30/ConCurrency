import sys
sys.path.append("src/proto/")

from proto.schema_pb2 import *
from proto.schema_pb2_grpc import *  # grpc is imported here


if __name__ == "__main__":
    request = GetBlockRequest(
            hash="0"*64
        )
    channel = grpc.insecure_channel('localhost:50001')
    stub =  NetworkStub(channel)
    received_block = stub.get_block(request)
    print("\nclient received this from the server:\n", received_block)
    pass