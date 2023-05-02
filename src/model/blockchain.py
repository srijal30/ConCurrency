"""
File where all the blockchain data model functionality will be stored
"""

from typing import Dict, List
from model.proto.schema_pb2 import Transaction, Block, BlockChain, Snapshot
from model.crypto import hash_block, hash_transaction, validate_signature, load_public_key
from model.proto.schema_pb2 import *
from threading import Lock

class TalkingStick():
    # should automatically make a genesis block if it is empty
    def __init__(self):
        self.blockchain = BlockChain()
        self.trans_pool: Dict[str, Transaction] = [] 
        self.uncommitted_snapshot = Snapshot()
        self.committed_snapshot = Snapshot()
        self._lock = Lock()

    ### BLOCK
    def validate_block(self, block:Block, snap : Snapshot = None) -> bool:
        """Validates block hash correctness and transaction validity. Assumes commited_snapshot is valid."""
        if self.calculate_difficulty() != block.difficulty:
            return False
        if self.calculate_reward() != block.reward:
            return False
        if block.curr_hash != hash_block(block) or block.curr_hash[0:block.difficulty] != "0"*block.difficulty:
            return False
        added_transactions = []
        for tran in block.trans:
            added_transactions.append(tran)
            # check if transaction is valid and amount is valid
            if snap == None:  # committed snapshot
                if not self._validate_snapshot(self.committed_snapshot, tran, added_transactions):
                    return False
            else:
                if not self._validate_snapshot(snap, tran, added_transactions):
                    return False
        return True
    

    ### TRANSACTION
    def validate_snapshot(self, snap : Snapshot, tran: Transaction, trans_list : List[Transaction]) -> bool:
        """Returns False if the transaction is invalid, true otherwise"""
        if not self.validate_transaction(tran) or not self.replay_committed(tran):
            # revert
            for added_tran in reversed(trans_list):
                self.undo_transaction(snap, added_tran)
            # return false
            return False
        return True
        
    def validate_transaction(self, tran: Transaction) -> bool:
        """Validates a transaction's signature and hash."""
        # validate the hash
        if not tran.hash == hash_transaction(tran):
            return False
        # validate the signature
        if not validate_signature(tran.signature, tran.hash, load_public_key(tran.sender_pub_key)):
            return False
        return True
    
    
    ### BLOCKCHAIN
    def validate_chain(self) -> bool:
        # loop through blockchain array and validate each block
        cur_snapshot = Snapshot()
        prev_hash = None
        for block in self.blockchain.blocks:
            # Check if previos hash matches the hash of the previous block
            if prev_hash is not None and block.prev_hash != prev_hash:
                return False
            # Check if the block is valid
            if not self.validate_block(block):
                return False
            prev_hash = block.curr_hash
        return True
        
    
    def add_block(self, block:Block) -> bool:
        """Adds block to the blockchain if valid. Returns whether operation was success. Also updates the committed snapshot."""    
        # Check block validity
        if not self.validate_block(block):
           return False
        # Update the blockchain with new block
        self._lock.acquire()
        self.blockchain.blocks.append(block)
        self._lock.release()
        return True
    
    
    def calculate_difficulty(self) -> int:
        """Calculates the difficulty for the next block."""
        return 5
    
    
    def calculate_reward(self)-> int:
        """Calculates the mining reward for the next block"""
        return 100
    

    ### SNAPSHOT

    def _validate_snapshot(self, snap : Snapshot, tran: Transaction, trans_list : List[Transaction]) -> bool:
        """Returns False if the transaction is invalid, true otherwise"""
        if not self.validate_transaction(tran) or not self.replay_committed(tran):
            # revert
            for added_tran in reversed(trans_list):
                self.undo_transaction(snap, added_tran)
            # return false
            return False
        return True

    def replay_committed(self, tran: Transaction) -> bool:
        """Does _replay_transaction on committed snapshot"""
        self._lock.acquire()
        result : bool = self._replay_transaction(self, self.committed_snapshot, tran)
        self._lock.release()
        return result
    
    def replay_uncommitted(self, tran: Transaction) -> bool:
        """Does _replay_transaction on uncommitted snapshot"""
        self._lock.acquire() 
        result : bool = self._replay_transaction(self, self.uncommitted_snapshot, tran)
        self._lock.release()
        return result
    
    def _replay_transaction(self, snapshot: Snapshot, tran: Transaction) ->  bool:
        """Checks if sequence number is correct, and that the exchange of coins is valid. Returns true if transaction added to Snapshot successfully."""
        # check if sequence is correct
        if tran.sequence != snapshot.accounts[tran.sender_pub_key].sequence:
            return False
        # send amount to receiver if sender has enough (and update sequence)
        if snapshot.accounts[tran.sender_pub_key].balance >= tran.amount:
            snapshot.accounts[tran.sender_pub_key].sequence += 1
            snapshot.accounts[tran.receiver_pub_key].balance += tran.amount
            snapshot.accounts[tran.sender_pub_key].balance -= tran.amount
            return True
        else:
            return False
    
 
    def undo_transaction(self, snapshot: Snapshot, tran: Transaction) -> None:
        """Undoes the effects of a transaction on snapshot"""
        self._lock.acquire()
        snapshot.accounts[tran.sender_pub_key].sequence -= 1
        snapshot.accounts[tran.receiver_pub_key].balance -= tran.amount
        snapshot.accounts[tran.sender_pub_key].balance += tran.amount
        self._lock.release()
    

    ### MINING POOL
    def pool_add(self, tran : Transaction) -> None:
        """Adds transaction to mining pool"""
        self._lock.acquire()
        self.trans_pool[tran.hash] = tran
        self._lock.release()
        return
    
    
    def pool_has(self, hash : str):
        self._lock.acquire()
        self._lock.release()
        return hash in self.trans_pool
    
    
    def pool_remove(self, hash : str) -> None:
        self._lock.acquire()
        del self.trans_pool[hash]
        self._lock.release() 
        return
    