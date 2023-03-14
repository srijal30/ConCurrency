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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cschema.proto\x12\x08messages\"-\n\nBlockChain\x12\x1f\n\x06\x62locks\x18\x01 \x03(\x0b\x32\x0f.messages.Block\"w\n\x05\x42lock\x12\x11\n\tprev_hash\x18\x01 \x01(\t\x12\x11\n\tcurr_hash\x18\x02 \x01(\t\x12\r\n\x05nonce\x18\x03 \x01(\x04\x12\x13\n\x0bmerkle_root\x18\x04 \x01(\t\x12$\n\x05trans\x18\x05 \x03(\x0b\x32\x15.messages.Transaction\"\x82\x01\n\x0bTransaction\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12\x16\n\x0esender_pub_key\x18\x02 \x01(\t\x12\x18\n\x10receiver_pub_key\x18\x03 \x01(\t\x12\x11\n\tsignature\x18\x04 \x01(\t\x12\x0e\n\x06\x61mount\x18\x05 \x01(\x04\x12\x10\n\x08sequence\x18\x06 \x01(\x04\"\x82\x01\n\x08Snapshot\x12\x32\n\x08\x61\x63\x63ounts\x18\x01 \x03(\x0b\x32 .messages.Snapshot.AccountsEntry\x1a\x42\n\rAccountsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.messages.Account:\x02\x38\x01\",\n\x07\x41\x63\x63ount\x12\x0f\n\x07\x62\x61lance\x18\x01 \x01(\x04\x12\x10\n\x08sequence\x18\x02 \x01(\x04\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'schema_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SNAPSHOT_ACCOUNTSENTRY._options = None
  _SNAPSHOT_ACCOUNTSENTRY._serialized_options = b'8\001'
  _globals['_BLOCKCHAIN']._serialized_start=26
  _globals['_BLOCKCHAIN']._serialized_end=71
  _globals['_BLOCK']._serialized_start=73
  _globals['_BLOCK']._serialized_end=192
  _globals['_TRANSACTION']._serialized_start=195
  _globals['_TRANSACTION']._serialized_end=325
  _globals['_SNAPSHOT']._serialized_start=328
  _globals['_SNAPSHOT']._serialized_end=458
  _globals['_SNAPSHOT_ACCOUNTSENTRY']._serialized_start=392
  _globals['_SNAPSHOT_ACCOUNTSENTRY']._serialized_end=458
  _globals['_ACCOUNT']._serialized_start=460
  _globals['_ACCOUNT']._serialized_end=504
# @@protoc_insertion_point(module_scope)