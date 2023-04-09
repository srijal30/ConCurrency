import sys
sys.path.append("src/model/proto/")

import concurrent.futures as futures
from typing import List

from model.loader import load_blockchain, store_blockchain
from model.proto.schema_pb2_grpc import *  # grpc is imported here
from model.proto.schema_pb2 import *


if __name__ == "__main__":
    try:
        blockchain = load_blockchain("blockchain.data")
        test_block = Block(
                curr_hash="1"*64,
                prev_hash="0"*64,
                miner_pub_key="Satoshi Nakamoto"  
        )
        blockchain.blocks.append(test_block)
        pool : List[Transaction] = []
        # starting the server
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        #service = Network(blockchain, Snapshot(), Snapshot(), pool) 
        print('here')
        service = Network()
        add_NetworkServicer_to_server(service, server)
        server.add_insecure_port("[::]:50001")
        server.start()
        server.wait_for_termination()
    except:
        print("server died")
        store_blockchain(blockchain, "blockchain.data")
        raise