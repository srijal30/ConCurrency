"""
File that contains the networking functions
"""

from model.proto.schema_pb2_grpc import NetworkServicer
from model.proto.schema_pb2 import *
from model.blockchain import TalkingStick
from threading import get_ident

class Network(NetworkServicer):
    # the arguments should all be wrapper classes w/ locks
    def __init__(self, stick: TalkingStick) -> None:
        self.model: TalkingStick = stick

    # make this take the callback
    def announce_block(self, request: AnnounceBlockRequest, context) -> AnnounceBlockReply:
        """Adds announced block to the chain if it is valid."""
        print("someone elsed finished mining first")
        print(request.block)
        new_block = request.block
        latest_hash = self.model.blockchain.blocks[-1].curr_hash
        # verify that the latest block is correct
        if new_block.prev_hash == latest_hash and self.model.validate_block(new_block):
            # add the block
            self.model.add_block(new_block)
            # tie loose ends with uncommited snapshot and transaction pool
            # THIS NEEDS REVIEW (maybe move this functionality to datamodel)
            for tran in new_block.trans:
                if self.model.pool_has(tran.hash):
                    self.model.pool_remove(tran.hash)
                else:
                    self.model.replay_uncommitted(tran)
        return AnnounceBlockReply()


    def send_transaction(self, request: SendTransactionRequest, context) -> SendTransactionReply:
        """Adds transaction to transaction pool if it is valid. Also updates uncommited snapshot."""
        new_tran = request.transaction
        if self.model.validate_transaction(new_tran) and self.model.replay_uncommitted(new_tran):
            self.model.pool_add(new_tran)
        return SendTransactionReply()    


    # inefficient
    def get_block(self, request: GetBlockRequest, context) -> GetBlockReply:
        """Returns block with requested hash if found. Else returns KeyError."""
        for block in self.model.blockchain.blocks:
            if block.curr_hash == request.hash:
                return GetBlockReply(
                    block=block
                )
        raise KeyError
    

    # inefficient
    def request_transaction(self, request: RequestTransactionRequest, context) -> RequestTransactionReply:
        """Returns transaction with requested hash if found. Else returns KeyError"""
        for block in self.model.blockchain.blocks:
            for tran in block.trans:
                if tran.hash == request.hash:
                    return RequestTransactionReply(
                        transaction=tran
                    )
        raise KeyError