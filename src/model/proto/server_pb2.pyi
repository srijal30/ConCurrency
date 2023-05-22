from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetIpListReply(_message.Message):
    __slots__ = ["ip_list"]
    IP_LIST_FIELD_NUMBER: _ClassVar[int]
    ip_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ip_list: _Optional[_Iterable[str]] = ...) -> None: ...

class GetIpListRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class InitiateConnectionReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class InitiateConnectionRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PingServerReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PingServerRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
