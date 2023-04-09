import sys
sys.path.append("src/model/proto/")

import concurrent.futures as futures
from typing import List
import grpc

from model.loader import load_blockchain, store_blockchain
from networking import Network
from model.blockchain import TalkingStick
from model.proto.schema_pb2_grpc import add_NetworkServicer_to_server
from model.proto.schema_pb2 import *


if __name__ == "__main__":
    try:
        # set up the model
        model = TalkingStick()
        test_block = Block(
                curr_hash="1"*64,
                prev_hash="0"*64,
                miner_pub_key="Satoshi Nakamoto"  
        )
        model.blockchain.blocks.append(test_block)
        print(model.blockchain)
        
        # start the server
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        service = Network(model)
        add_NetworkServicer_to_server(service, server)
        server.add_insecure_port("[::]:50001")
        server.start()
        server.wait_for_termination()

    except:
        print("server died")
        store_blockchain(model.blockchain, "blockchain.data")
        raise