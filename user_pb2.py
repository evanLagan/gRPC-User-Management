# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: user.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'user.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\"D\n\x0fRegisterRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\"1\n\rRegisterReply\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x1e\n\x0bUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"=\n\tUserReply\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"2\n\x0cLoginRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"=\n\nLoginReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\r\n\x05token\x18\x03 \x01(\t\"\x07\n\x05\x45mpty2\xb4\x01\n\x0bUserService\x12\x32\n\x0cRegisterUser\x12\x10.RegisterRequest\x1a\x0e.RegisterReply\"\x00\x12%\n\x07GetUser\x12\x0c.UserRequest\x1a\n.UserReply\"\x00\x12#\n\tListUsers\x12\x06.Empty\x1a\n.UserReply\"\x00\x30\x01\x12%\n\x05Login\x12\r.LoginRequest\x1a\x0b.LoginReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REGISTERREQUEST']._serialized_start=14
  _globals['_REGISTERREQUEST']._serialized_end=82
  _globals['_REGISTERREPLY']._serialized_start=84
  _globals['_REGISTERREPLY']._serialized_end=133
  _globals['_USERREQUEST']._serialized_start=135
  _globals['_USERREQUEST']._serialized_end=165
  _globals['_USERREPLY']._serialized_start=167
  _globals['_USERREPLY']._serialized_end=228
  _globals['_LOGINREQUEST']._serialized_start=230
  _globals['_LOGINREQUEST']._serialized_end=280
  _globals['_LOGINREPLY']._serialized_start=282
  _globals['_LOGINREPLY']._serialized_end=343
  _globals['_EMPTY']._serialized_start=345
  _globals['_EMPTY']._serialized_end=352
  _globals['_USERSERVICE']._serialized_start=355
  _globals['_USERSERVICE']._serialized_end=535
# @@protoc_insertion_point(module_scope)
