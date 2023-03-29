from proto.schema_pb2 import *

def store_blockchain(chain: BlockChain, path: str) -> None:
    with open(path, 'wb') as file:
        file.write(chain.SerializeToString())

def load_blockchain(path: str) -> BlockChain:
    try:
        with open(path, 'rb') as file:
            chain = BlockChain()
            chain.ParseFromString(file.read())
            return chain
    except:
        print("Empty Blockchain")
        return BlockChain()