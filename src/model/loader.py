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
    """stores block to file"""
    with open(path, 'ab') as file:
        file.write(block.SerializeToString())
