from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BlockChain(_message.Message):
    __slots__ = ["blocks"]
    BLOCKS_FIELD_NUMBER: _ClassVar[int]
    blocks: _containers.RepeatedCompositeFieldContainer[Block]
    def __init__(self, blocks: _Optional[_Iterable[_Union[Block, _Mapping]]] = ...) -> None: ...

class Block(_message.Message):
    __slots__ = ["prev_hash", "curr_hash", "nonce", "merkle_root", "trans"]
    PREV_HASH_FIELD_NUMBER: _ClassVar[int]
    CURR_HASH_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    MERKLE_ROOT_FIELD_NUMBER: _ClassVar[int]
    TRANS_FIELD_NUMBER: _ClassVar[int]
    prev_hash: str
    curr_hash: str
    nonce: int
    merkle_root: str
    trans: _containers.RepeatedCompositeFieldContainer[Transaction]
    def __init__(self, prev_hash: _Optional[str] = ..., curr_hash: _Optional[str] = ..., nonce: _Optional[int] = ..., merkle_root: _Optional[str] = ..., trans: _Optional[_Iterable[_Union[Transaction, _Mapping]]] = ...) -> None: ...

class Transaction(_message.Message):
    __slots__ = ["hash", "sender_pub_key", "receiver_pub_key", "signature", "amount", "sequence"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    SENDER_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    hash: str
    sender_pub_key: str
    receiver_pub_key: str
    signature: str
    amount: int
    sequence: int
    def __init__(self, hash: _Optional[str] = ..., sender_pub_key: _Optional[str] = ..., receiver_pub_key: _Optional[str] = ..., signature: _Optional[str] = ..., amount: _Optional[int] = ..., sequence: _Optional[int] = ...) -> None: ...

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

class Account(_message.Message):
    __slots__ = ["balance", "sequence"]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    balance: int
    sequence: int
    def __init__(self, balance: _Optional[int] = ..., sequence: _Optional[int] = ...) -> None: ...
