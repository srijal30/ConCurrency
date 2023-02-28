"""
File where all the crypto functionality will be stored
"""

# TO DO:
# change type of signature to hex

from typing import Any, Tuple
from schema_pb2 import Block
from hashlib import sha256

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.rsa import (
    generate_private_key,
    RSAPrivateKey,
    RSAPublicKey
)

# should I change these? currently using the config from documentation.
EXPONENT = 65537
KEY_SIZE = 512
ALGORITHM = hashes.SHA256()
PADDING = padding.PSS(
            mgf=padding.MGF1(ALGORITHM),
            salt_length=padding.PSS.MAX_LENGTH
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
        public_exponent=EXPONENT,
        key_size=KEY_SIZE
    )
    pub_key : RSAPublicKey = priv_key.public_key()
    return (priv_key, pub_key)


# TO DO: fix error where if user inputs str that cannout be converted to hex, an exception is raised
def validate_signature(signature: str, message: str, pub_key : RSAPublicKey) -> bool:
    """Validates an RSA signature using OpenSSL."""
    try:
        pub_key.verify(
            signature=bytes.fromhex(signature), # converting from hex to bytes
            data=message.encode(), # converting from str to bytes
            padding=PADDING,
            algorithm=ALGORITHM
        )
        return True
    except InvalidSignature:
        return False


def create_signature(message: str, priv_key: RSAPrivateKey) -> str:
    """Creates and returns an RSA signature using OpenSSL. The signature will be in hex."""
    signature =  priv_key.sign(
        data=message.encode(),
        padding=PADDING,
        algorithm=ALGORITHM
    )
    return signature.hex()


# TESTING
if __name__ == "__main__":
    priv, pub = create_keys()
    msg = "hello"
    sig = create_signature(msg, priv)
    
    # right signature
    print(validate_signature(sig, msg, pub))

    # wrong signature
    fake_sig = hash("Hi")
    print(validate_signature(fake_sig, msg, pub))