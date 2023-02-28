"""
File where all the crypto functionality will be stored
"""

from typing import Any, Tuple
from schema_pb2 import Block

from hashlib import sha256
from cryptography.hazmat.primitives.asymmetric.rsa import (
    generate_private_key,
    RSAPrivateKey,
    RSAPublicKey
)

def hash(*args: Any) -> str:
    """Hashes the input using sha256"""
    msg = ""
    for arg in args:
        msg += str(arg)
    hash = sha256(msg.encode())
    return hash.hexdigest()


def hash_block(block: Block) -> str:
    """Returns the hash of the block's contents."""
    return hash(
        block.prev_hash,
        block.nonce,
        block.merkle_root
    )


def create_keys() -> Tuple[RSAPrivateKey, RSAPublicKey]:
    """
    Creates and returns keypair using OpenSSL's RSA algorithm.
    """
    priv_key : RSAPrivateKey = generate_private_key(
        public_exponent=65537,
        key_size=2
    )
    pub_key : RSAPublicKey = priv_key.public_key()
    return (priv_key, pub_key)


def validate_signature(signature: str, pub_key : RSAPublicKey) -> bool:
    """Validates an RSA signature using OpenSSL"""
    return False


def create_signature(message: str, priv_key: RSAPrivateKey) -> str:
    """Creates and returns an RSA signature using OpenSSL"""
    return False