"""
text script to test transactions to local nodes via grpc

Run this in diff terminal while the node is running:
    python src/send_tx.py
"""

import grpc
from model.proto.schema_pb2 import Transaction, AnnounceTransactionRequest
from model.proto.schema_pb2_grpc import NetworkStub

from model.crypto import (
    create_keys,
    create_signature,
    hash_transaction,
    serialize_public_key,
)


def build_test_transaction():
    #makkin wallett
    priv_key, pub_key = create_keys()
    sender_pub_pem = serialize_public_key(pub_key)

    #testing by self pass
    receiver_pub_pem = sender_pub_pem

    #build trans
    tx = Transaction(
        sender_pub_key=sender_pub_pem,
        receiver_pub_key=receiver_pub_pem,
        amount=0,
        sequence=0,
    )

    tx_hash = hash_transaction(tx)
    tx.hash = tx_hash

    #sign with key
    signature_hex = create_signature(tx_hash, priv_key)
    tx.signature = signature_hex

    return tx


def main():

    tx = build_test_transaction()
    print(f"[WALLET] Built tx {tx.hash[:16]}..., amount={tx.amount}, seq={tx.sequence}")

    #local node for now for testing
    channel = grpc.insecure_channel("localhost:50001")
    stub = NetworkStub(channel)
    request = AnnounceTransactionRequest(transaction=tx)
    stub.announce_transaction(request)

    print("[WALLET] Sent transaction to node")


if __name__ == "__main__":
    main()
