"""
File that contains the networking functions
"""

import sys
sys.path.append("src/proto/")

import grpc
import concurrent.futures as futures
from proto.schema_pb2_grpc import NetworkServicer, NetworkStub, add_NetworkServicer_to_server
from proto.schema_pb2 import *
from blockchain import *
from crypto import *
from loader import *

# TO DO: 
# - type definitions

class Network(NetworkServicer):
    # the arguments should all be wrapper classes w/ locks
    def __init__(self, chain, snap1, snap2, pool):
        self.blockchain = chain
        self.uncommitted_snap = snap1
        self.committed_snap = snap2
        self.transaction_pool = pool

    def announce_block(self, request: AnnounceBlockRequest, context) -> AnnounceBlockReply:
        """Adds announced block to the chain if it is valid."""
        latest_block_hash = self.blockchain.blocks[-1].curr_hash
        if request.block.prev_hash == latest_block_hash and validate_block(request.block):
            # add the block

            # self.blockchain.lock()
            # self.committed_snap.lock()
            add_block(self.committed_snap, request.block, self.blockchain)
            # self.blockchain.unlock()
            # self.committed_snap.unlock()
            
            # tie loose ends with uncommited snapshot and transaction pool
            # THIS NEEDS REVIEW (also maybe add this functionality to datamodel)
            
            # self.transaction_pool.lock()
            # self.uncommitted_snap.lock()
            for tran in request.block.trans:
                if tran in self.transaction_pool: # will this code even work? will this compare memory addresses?
                    self.transaction_pool.remove(tran)
                else: # if not in transaction pool, it means we have to add it to uncommited snapshot
                    replay_transaction(self.uncommitted_snapshot, tran)
            # self.transaction_pool.unlock()
            # self.uncommitted_snap.unlock()
        return AnnounceBlockReply()
    
    def send_transaction(self, request: SendTransactionRequest, context) -> SendTransactionReply:
        """Adds transaction to transaction pool if it is valid. Also updates uncommited snapshot."""
        # self.uncommitted_snap.lock()
        if validate_transaction(request.transaction) and replay_transaction(self.uncommitted_snap, request.transaction):
            # self.transaction_pool.lock()
            self.transaction_pool.append(request.transaction)
            # self.transaction_pool.unlock()
        # self.uncommitted_snap.unlock()
        return SendTransactionReply()    

    def get_block(self, request: GetBlockRequest, context) -> GetBlockReply:
        """Returns block with requested hash if found."""
        for block in self.blockchain.blocks:
            if block.curr_hash == request.hash:
                return GetBlockReply(
                    block=block
                )
        raise KeyError
    
    def request_transaction(self, request: RequestTransactionRequest, context) -> RequestTransactionReply:
        """Returns transaction with requested hash if found."""
        for block in self.blockchain.blocks:
            for tran in block.trans:
                if tran.hash == request.hash:
                    return RequestTransactionReply(
                        transaction=tran
                    )
        return RequestTransactionReply()


# QUICK TEST THAT REQUESTS BLOCK FROM SERVER
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
        service = Network(blockchain, Snapshot(), Snapshot(), pool)
        add_NetworkServicer_to_server(service, server)
        server.add_insecure_port("[::]:50001")
        server.start()
        server.wait_for_termination()
    except:
        print("server died")
        store_blockchain(blockchain, "blockchain.data")
        raise