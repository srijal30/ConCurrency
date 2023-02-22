"""
File where all the cryptography functionality will be stored
"""

from typing import Any, Tuple
from hashlib import sha256

# TO DO: make this work with datas structures like block and transaction
def hash(*args: Any) -> str:
    """Hashes the input using sha256"""
    msg = ""
    for arg in args:
        msg += str(arg)
    hash = sha256(msg.encode())
    return hash.hexdigest()

#maybe create seperate hashing functions for each datatype that needs to be hashed?

def create_keys() -> Tuple[int, int]:
    """
    Creates a keypair using OpenSSL's RSA algorithm.
    - index 0 is the public key
    - index 1 is the private key
    """
    return (0, 0)

def validate_signature(signature: str, pub_key : None) -> bool:
    """Validates an RSA signature using OpenSSL"""
    return False

def create_signature(message: str, priv_key: None) -> str:
    """Creates and returns an RSA signature using OpenSSL"""
    return False