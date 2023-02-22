"""
File where all the blockchain data model functionality will be stored
"""

from schema_pb2 import Transaction
from crypto import validate_signature

def validate_transaction(tran: Transaction) -> bool:
    """Validates a transaction"""
    # validate the signature
    if not validate_signature(tran.signature, tran.sender_pub_key):
        return False
    
    # TO DO: validate the amount
    # ...
    
    return True