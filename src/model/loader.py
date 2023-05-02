from model.proto.schema_pb2 import *

def store_blockchain(chain: BlockChain, path: str) -> None:
    """Serializes and dumps blockchain into the specified file."""
    with open(path, 'wb') as file:
        file.write(chain.SerializeToString())


def load_blockchain(path: str) -> BlockChain:
    """Loads a blockchain from a file."""
    try:
        with open(path, 'rb') as file:
            chain = BlockChain()
            chain.ParseFromString(file.read())
            return chain
    except:
        print("Empty Blockchain")
        return BlockChain()


def store_block(block: Block, path: str) -> None:
    """Stores block to file by appending."""
    with open(path, 'ab') as file:
        file.write(block.SerializeToString())


def store_snapshot(snapshot: Snapshot, path: str) -> None:
    """Serializes and dumps blockchain into the specified file."""
    with open(path, 'wb') as file:
        file.write(snapshot.SerializeToString())


def load_snapshot(path: str) -> Snapshot:
    try:
        with open(path, 'rb') as file:
            snap = Snapshot()
            snap.ParseFromString(file.read())
            return snap
    except:
        print("Empty Snapshot")
        return Snapshot()