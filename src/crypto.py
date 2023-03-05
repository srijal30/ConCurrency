"""
File where all the crypto functionality will be stored
"""

from typing import Any, Tuple, List
from schema_pb2 import Block, Transaction
from hashlib import sha256

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.rsa import (
    generate_private_key,
    RSAPrivateKey,
    RSAPublicKey
)

EXPONENT = 65537
KEY_SIZE = 512
ALGORITHM = hashes.SHA256()
PADDING = padding.PSS(
            mgf=padding.MGF1(ALGORITHM),
            salt_length=padding.PSS.MAX_LENGTH
        )
ENCODING = serialization.Encoding.PEM
PRIVATE_FORMAT = serialization.PrivateFormat.TraditionalOpenSSL
PUBLIC_FORMAT = serialization.PublicFormat.SubjectPublicKeyInfo


### HASHING

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


def hash_transaction(tran: Transaction) -> str:
    """Returns the has of the transaction's contents."""
    return hash(
        tran.receiver_pub_key,
        tran.amount,
        tran.sequence
    )

def merkle_root(transactions: List[Transaction]) -> str:
    """Recursively creates the merkle root and returns it."""
    transaction_hashes = [t.hash for t in transactions]
    def root_helper(hashes: List[str]) -> str:
        if len(hashes) == 1:
            return hashes[0]
        new_len = len(hashes)/2
        for i in range(new_len):
            hashes[i] = hash(hashes[i] + hashes.pop(i+1))
    return root_helper(transaction_hashes)

### RSA Functions

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


def validate_signature(signature: str, message: str, pub_key : RSAPublicKey) -> bool:
    """Validates an RSA signature using OpenSSL. Signaure must be valid hex string."""
    try:
        pub_key.verify(
            signature=bytes.fromhex(signature), # converting from hexstring to bytes
            data=message.encode(), # converting from str to bytes
            padding=PADDING,
            algorithm=ALGORITHM
        )
        return True
    except (ValueError, InvalidSignature):
        return False


def create_signature(message: str, priv_key: RSAPrivateKey) -> str:
    """Creates and returns an RSA signature using OpenSSL. The signature will be a hex string."""
    signature =  priv_key.sign(
        data=message.encode(),
        padding=PADDING,
        algorithm=ALGORITHM
    )
    return signature.hex()


def serialize_public_key(pub_key: RSAPublicKey) -> str:
    """Converts public key from RSAPublicKey object to PEM format."""
    pem = pub_key.public_bytes(
        encoding=ENCODING,
        format=PUBLIC_FORMAT
    )
    return pem.decode()


def load_public_key(pub_key: str) -> RSAPublicKey | None:
    """Converts public key from PEM format to the object RSAPublicKey. If input is not valid, returns None."""
    try:
        pub = serialization.load_pem_public_key(pub_key.encode())
        assert isinstance(pub, RSAPublicKey)
        return pub
    except ValueError:
        return None


### TESTING

if __name__ == "__main__":
    priv, pub = create_keys()
    msg = "hello"
    sig = create_signature(msg, priv)
    
    # right signature
    print(validate_signature(sig, msg, pub))

    # wrong signature
    fake_sig = 'hi'
    print(validate_signature(fake_sig, msg, pub))

    # serialize the public key
    serial = serialize_public_key(pub)
    print(serial)

    # unserialize the public key
    unserial = load_public_key(serial)
    if unserial:
        print(pub.public_numbers() == unserial.public_numbers())