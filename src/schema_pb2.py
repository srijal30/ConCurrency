# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: schema.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cschema.proto\"#\n\nBlockChain\x12\x15\n\x05\x62lock\x18\x01 \x03(\x0b\x32\x06.Block\"{\n\x05\x42lock\x12\x11\n\tprev_hash\x18\x01 \x01(\x04\x12\x11\n\tcurr_hash\x18\x02 \x01(\x04\x12\r\n\x05nonce\x18\x03 \x01(\x04\x12\x0b\n\x03pow\x18\x04 \x01(\x04\x12\x13\n\x0bmerkle_root\x18\x05 \x01(\x04\x12\x1b\n\x05trans\x18\x06 \x03(\x0b\x32\x0c.Transaction\"b\n\x0bTransaction\x12\x16\n\x0esender_pub_key\x18\x01 \x01(\t\x12\x18\n\x10receiver_pub_key\x18\x02 \x01(\t\x12\x11\n\tsignature\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x04\"\n\n\x08Snapshotb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'schema_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_BLOCKCHAIN']._serialized_start=16
  _globals['_BLOCKCHAIN']._serialized_end=51
  _globals['_BLOCK']._serialized_start=53
  _globals['_BLOCK']._serialized_end=176
  _globals['_TRANSACTION']._serialized_start=178
  _globals['_TRANSACTION']._serialized_end=276
  _globals['_SNAPSHOT']._serialized_start=278
  _globals['_SNAPSHOT']._serialized_end=288
# @@protoc_insertion_point(module_scope)