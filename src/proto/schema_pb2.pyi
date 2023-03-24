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

class Block(_message.Message):
    __slots__ = ["curr_hash", "difficulty", "merkle_root", "miner", "mining_reward", "nonce", "prev_hash", "trans"]
    CURR_HASH_FIELD_NUMBER: _ClassVar[int]
    DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    MERKLE_ROOT_FIELD_NUMBER: _ClassVar[int]
    MINER_FIELD_NUMBER: _ClassVar[int]
    MINING_REWARD_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    PREV_HASH_FIELD_NUMBER: _ClassVar[int]
    TRANS_FIELD_NUMBER: _ClassVar[int]
    curr_hash: str
    difficulty: int
    merkle_root: str
    miner: str
    mining_reward: int
    nonce: int
    prev_hash: str
    trans: _containers.RepeatedCompositeFieldContainer[Transaction]
    def __init__(self, prev_hash: _Optional[str] = ..., curr_hash: _Optional[str] = ..., nonce: _Optional[int] = ..., merkle_root: _Optional[str] = ..., trans: _Optional[_Iterable[_Union[Transaction, _Mapping]]] = ..., miner: _Optional[str] = ..., mining_reward: _Optional[int] = ..., difficulty: _Optional[int] = ...) -> None: ...

class BlockChain(_message.Message):
    __slots__ = ["blocks"]
    BLOCKS_FIELD_NUMBER: _ClassVar[int]
    blocks: _containers.RepeatedCompositeFieldContainer[Block]
    def __init__(self, blocks: _Optional[_Iterable[_Union[Block, _Mapping]]] = ...) -> None: ...

class GetBlockReply(_message.Message):
    __slots__ = ["blocks"]
    BLOCKS_FIELD_NUMBER: _ClassVar[int]
    blocks: _containers.RepeatedCompositeFieldContainer[Block]
    def __init__(self, blocks: _Optional[_Iterable[_Union[Block, _Mapping]]] = ...) -> None: ...

class GetBlockRequest(_message.Message):
    __slots__ = ["hashes"]
    HASHES_FIELD_NUMBER: _ClassVar[int]
    hashes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, hashes: _Optional[_Iterable[str]] = ...) -> None: ...

class SendBlockchainReply(_message.Message):
    __slots__ = ["cur_block", "latest_block"]
    CUR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    LATEST_BLOCK_FIELD_NUMBER: _ClassVar[int]
    cur_block: Block
    latest_block: bool
    def __init__(self, cur_block: _Optional[_Union[Block, _Mapping]] = ..., latest_block: bool = ...) -> None: ...

class SendBlockchainRequest(_message.Message):
    __slots__ = ["since_hash"]
    SINCE_HASH_FIELD_NUMBER: _ClassVar[int]
    since_hash: str
    def __init__(self, since_hash: _Optional[str] = ...) -> None: ...

class SendTransactionReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SendTransactionRequest(_message.Message):
    __slots__ = ["trans"]
    TRANS_FIELD_NUMBER: _ClassVar[int]
    trans: _containers.RepeatedCompositeFieldContainer[Transaction]
    def __init__(self, trans: _Optional[_Iterable[_Union[Transaction, _Mapping]]] = ...) -> None: ...

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
