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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cschema.proto\x12\x08messages\"-\n\nBlockChain\x12\x1f\n\x06\x62locks\x18\x01 \x03(\x0b\x32\x0f.messages.Block\"w\n\x05\x42lock\x12\x11\n\tprev_hash\x18\x01 \x01(\t\x12\x11\n\tcurr_hash\x18\x02 \x01(\t\x12\r\n\x05nonce\x18\x03 \x01(\x04\x12\x13\n\x0bmerkle_root\x18\x04 \x01(\t\x12$\n\x05trans\x18\x05 \x03(\x0b\x32\x15.messages.Transaction\"\x82\x01\n\x0bTransaction\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12\x16\n\x0esender_pub_key\x18\x02 \x01(\t\x12\x18\n\x10receiver_pub_key\x18\x03 \x01(\t\x12\x11\n\tsignature\x18\x04 \x01(\t\x12\x0e\n\x06\x61mount\x18\x05 \x01(\x04\x12\x10\n\x08sequence\x18\x06 \x01(\x04\"\x82\x01\n\x08Snapshot\x12\x32\n\x08\x61\x63\x63ounts\x18\x01 \x03(\x0b\x32 .messages.Snapshot.AccountsEntry\x1a\x42\n\rAccountsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.messages.Account:\x02\x38\x01\",\n\x07\x41\x63\x63ount\x12\x0f\n\x07\x62\x61lance\x18\x01 \x01(\x04\x12\x10\n\x08sequence\x18\x02 \x01(\x04\"!\n\x0fGetBlockRequest\x12\x0e\n\x06hashes\x18\x01 \x03(\t\"0\n\rGetBlockReply\x12\x1f\n\x06\x62locks\x18\x01 \x03(\x0b\x32\x0f.messages.Block\"6\n\x14\x41nnounceBlockRequest\x12\x1e\n\x05\x62lock\x18\x01 \x01(\x0b\x32\x0f.messages.Block\"\x14\n\x12\x41nnounceBlockReply\">\n\x16SendTransactionRequest\x12$\n\x05trans\x18\x01 \x03(\x0b\x32\x15.messages.Transaction\"\x16\n\x14SendTransactionReply\"?\n\x15SendBlockchainRequest\x12\x17\n\nsince_hash\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\r\n\x0b_since_hash\"O\n\x13SendBlockchainReply\x12\"\n\tcur_block\x18\x01 \x01(\x0b\x32\x0f.messages.Block\x12\x14\n\x0clatest_block\x18\x02 \x01(\x08\x32\xd0\x02\n\nMiningNode\x12\x41\n\tget_block\x12\x19.messages.GetBlockRequest\x1a\x17.messages.GetBlockReply\"\x00\x12P\n\x0e\x61nnounce_block\x12\x1e.messages.AnnounceBlockRequest\x1a\x1c.messages.AnnounceBlockReply\"\x00\x12V\n\x10send_transaction\x12 .messages.SendTransactionRequest\x1a\x1e.messages.SendTransactionReply\"\x00\x12U\n\x0fsend_blockchain\x12\x1f.messages.SendBlockchainRequest\x1a\x1d.messages.SendBlockchainReply\"\x00\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'schema_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SNAPSHOT_ACCOUNTSENTRY._options = None
  _SNAPSHOT_ACCOUNTSENTRY._serialized_options = b'8\001'
  _BLOCKCHAIN._serialized_start=26
  _BLOCKCHAIN._serialized_end=71
  _BLOCK._serialized_start=73
  _BLOCK._serialized_end=192
  _TRANSACTION._serialized_start=195
  _TRANSACTION._serialized_end=325
  _SNAPSHOT._serialized_start=328
  _SNAPSHOT._serialized_end=458
  _SNAPSHOT_ACCOUNTSENTRY._serialized_start=392
  _SNAPSHOT_ACCOUNTSENTRY._serialized_end=458
  _ACCOUNT._serialized_start=460
  _ACCOUNT._serialized_end=504
  _GETBLOCKREQUEST._serialized_start=506
  _GETBLOCKREQUEST._serialized_end=539
  _GETBLOCKREPLY._serialized_start=541
  _GETBLOCKREPLY._serialized_end=589
  _ANNOUNCEBLOCKREQUEST._serialized_start=591
  _ANNOUNCEBLOCKREQUEST._serialized_end=645
  _ANNOUNCEBLOCKREPLY._serialized_start=647
  _ANNOUNCEBLOCKREPLY._serialized_end=667
  _SENDTRANSACTIONREQUEST._serialized_start=669
  _SENDTRANSACTIONREQUEST._serialized_end=731
  _SENDTRANSACTIONREPLY._serialized_start=733
  _SENDTRANSACTIONREPLY._serialized_end=755
  _SENDBLOCKCHAINREQUEST._serialized_start=757
  _SENDBLOCKCHAINREQUEST._serialized_end=820
  _SENDBLOCKCHAINREPLY._serialized_start=822
  _SENDBLOCKCHAINREPLY._serialized_end=901
  _MININGNODE._serialized_start=904
  _MININGNODE._serialized_end=1240
# @@protoc_insertion_point(module_scope)
