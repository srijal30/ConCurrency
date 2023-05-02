from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Account(_message.Message):
    __slots__ = ["balance", "sequence"]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    balance: int
    sequence: int
    def __init__(self, balance: _Optional[int] = ..., sequence: _Optional[int] = ...) -> None: ...

class AnnounceBlockReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AnnounceBlockRequest(_message.Message):
    __slots__ = ["block"]
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    block: Block
    def __init__(self, block: _Optional[_Union[Block, _Mapping]] = ...) -> None: ...

class AnnounceTransactionReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AnnounceTransactionRequest(_message.Message):
    __slots__ = ["transaction"]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    transaction: Transaction
    def __init__(self, transaction: _Optional[_Union[Transaction, _Mapping]] = ...) -> None: ...

class Block(_message.Message):
    __slots__ = ["curr_hash", "difficulty", "merkle_root", "miner_pub_key", "nonce", "prev_hash", "reward", "timestamp", "trans"]
    CURR_HASH_FIELD_NUMBER: _ClassVar[int]
    DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    MERKLE_ROOT_FIELD_NUMBER: _ClassVar[int]
    MINER_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    PREV_HASH_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TRANS_FIELD_NUMBER: _ClassVar[int]
    curr_hash: str
    difficulty: int
    merkle_root: str
    miner_pub_key: str
    nonce: int
    prev_hash: str
    reward: int
    timestamp: float
    trans: _containers.RepeatedCompositeFieldContainer[Transaction]
    def __init__(self, prev_hash: _Optional[str] = ..., curr_hash: _Optional[str] = ..., nonce: _Optional[int] = ..., merkle_root: _Optional[str] = ..., trans: _Optional[_Iterable[_Union[Transaction, _Mapping]]] = ..., miner_pub_key: _Optional[str] = ..., reward: _Optional[int] = ..., difficulty: _Optional[int] = ..., timestamp: _Optional[float] = ...) -> None: ...

class BlockChain(_message.Message):
    __slots__ = ["blocks"]
    BLOCKS_FIELD_NUMBER: _ClassVar[int]
    blocks: _containers.RepeatedCompositeFieldContainer[Block]
    def __init__(self, blocks: _Optional[_Iterable[_Union[Block, _Mapping]]] = ...) -> None: ...

class GetBlockReply(_message.Message):
    __slots__ = ["block"]
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    block: Block
    def __init__(self, block: _Optional[_Union[Block, _Mapping]] = ...) -> None: ...

class GetBlockRequest(_message.Message):
    __slots__ = ["hash"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    hash: str
    def __init__(self, hash: _Optional[str] = ...) -> None: ...

class GetChainLengthReply(_message.Message):
    __slots__ = ["length"]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    length: int
    def __init__(self, length: _Optional[int] = ...) -> None: ...

class GetChainLengthRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetChainReply(_message.Message):
    __slots__ = ["hashes"]
    HASHES_FIELD_NUMBER: _ClassVar[int]
    hashes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, hashes: _Optional[_Iterable[str]] = ...) -> None: ...

class GetChainRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetTransactionReply(_message.Message):
    __slots__ = ["transaction"]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    transaction: Transaction
    def __init__(self, transaction: _Optional[_Union[Transaction, _Mapping]] = ...) -> None: ...

class GetTransactionRequest(_message.Message):
    __slots__ = ["hash"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    hash: str
    def __init__(self, hash: _Optional[str] = ...) -> None: ...

class Snapshot(_message.Message):
    __slots__ = ["accounts"]
    class AccountsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Account
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Account, _Mapping]] = ...) -> None: ...
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    accounts: _containers.MessageMap[str, Account]
    def __init__(self, accounts: _Optional[_Mapping[str, Account]] = ...) -> None: ...

class Transaction(_message.Message):
    __slots__ = ["amount", "hash", "receiver_pub_key", "sender_pub_key", "sequence", "signature"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    SENDER_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    amount: int
    hash: str
    receiver_pub_key: str
    sender_pub_key: str
    sequence: int
    signature: str
    def __init__(self, hash: _Optional[str] = ..., sender_pub_key: _Optional[str] = ..., receiver_pub_key: _Optional[str] = ..., signature: _Optional[str] = ..., amount: _Optional[int] = ..., sequence: _Optional[int] = ...) -> None: ...
