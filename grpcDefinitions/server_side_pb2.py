# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server_side.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='server_side.proto',
  package='server_side',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11server_side.proto\x12\x0bserver_side\"$\n\x08ServerID\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x03\"x\n\nServerInfo\x12\x0e\n\x06source\x18\x01 \x01(\t\x12#\n\x04next\x18\x02 \x01(\x0b\x32\x15.server_side.ServerID\x12#\n\x04\x62\x61\x63k\x18\x03 \x01(\x0b\x32\x15.server_side.ServerID\x12\x10\n\x08serverID\x18\x04 \x01(\x03\"Z\n\x0b\x46ingerTable\x12%\n\x06source\x18\x01 \x01(\x0b\x32\x15.server_side.ServerID\x12$\n\x05table\x18\x02 \x03(\x0b\x32\x15.server_side.ServerID\"\x06\n\x04Void2\xce\x02\n\x03P2P\x12\x42\n\x0cgetNeighbors\x12\x17.server_side.ServerInfo\x1a\x17.server_side.ServerInfo\"\x00\x12:\n\x04\x65xit\x12\x17.server_side.ServerInfo\x1a\x17.server_side.ServerInfo\"\x00\x12:\n\x04join\x12\x17.server_side.ServerInfo\x1a\x17.server_side.ServerInfo\"\x00\x12J\n\x12\x62uild_finger_table\x12\x18.server_side.FingerTable\x1a\x18.server_side.FingerTable\"\x00\x12?\n\x0enotify_cluster\x12\x18.server_side.FingerTable\x1a\x11.server_side.Void\"\x00\x62\x06proto3')
)




_SERVERID = _descriptor.Descriptor(
  name='ServerID',
  full_name='server_side.ServerID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='server_side.ServerID.host', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='server_side.ServerID.id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=70,
)


_SERVERINFO = _descriptor.Descriptor(
  name='ServerInfo',
  full_name='server_side.ServerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='server_side.ServerInfo.source', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next', full_name='server_side.ServerInfo.next', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='back', full_name='server_side.ServerInfo.back', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serverID', full_name='server_side.ServerInfo.serverID', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=192,
)


_FINGERTABLE = _descriptor.Descriptor(
  name='FingerTable',
  full_name='server_side.FingerTable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='server_side.FingerTable.source', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='table', full_name='server_side.FingerTable.table', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=194,
  serialized_end=284,
)


_VOID = _descriptor.Descriptor(
  name='Void',
  full_name='server_side.Void',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=286,
  serialized_end=292,
)

_SERVERINFO.fields_by_name['next'].message_type = _SERVERID
_SERVERINFO.fields_by_name['back'].message_type = _SERVERID
_FINGERTABLE.fields_by_name['source'].message_type = _SERVERID
_FINGERTABLE.fields_by_name['table'].message_type = _SERVERID
DESCRIPTOR.message_types_by_name['ServerID'] = _SERVERID
DESCRIPTOR.message_types_by_name['ServerInfo'] = _SERVERINFO
DESCRIPTOR.message_types_by_name['FingerTable'] = _FINGERTABLE
DESCRIPTOR.message_types_by_name['Void'] = _VOID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServerID = _reflection.GeneratedProtocolMessageType('ServerID', (_message.Message,), dict(
  DESCRIPTOR = _SERVERID,
  __module__ = 'server_side_pb2'
  # @@protoc_insertion_point(class_scope:server_side.ServerID)
  ))
_sym_db.RegisterMessage(ServerID)

ServerInfo = _reflection.GeneratedProtocolMessageType('ServerInfo', (_message.Message,), dict(
  DESCRIPTOR = _SERVERINFO,
  __module__ = 'server_side_pb2'
  # @@protoc_insertion_point(class_scope:server_side.ServerInfo)
  ))
_sym_db.RegisterMessage(ServerInfo)

FingerTable = _reflection.GeneratedProtocolMessageType('FingerTable', (_message.Message,), dict(
  DESCRIPTOR = _FINGERTABLE,
  __module__ = 'server_side_pb2'
  # @@protoc_insertion_point(class_scope:server_side.FingerTable)
  ))
_sym_db.RegisterMessage(FingerTable)

Void = _reflection.GeneratedProtocolMessageType('Void', (_message.Message,), dict(
  DESCRIPTOR = _VOID,
  __module__ = 'server_side_pb2'
  # @@protoc_insertion_point(class_scope:server_side.Void)
  ))
_sym_db.RegisterMessage(Void)



_P2P = _descriptor.ServiceDescriptor(
  name='P2P',
  full_name='server_side.P2P',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=295,
  serialized_end=629,
  methods=[
  _descriptor.MethodDescriptor(
    name='getNeighbors',
    full_name='server_side.P2P.getNeighbors',
    index=0,
    containing_service=None,
    input_type=_SERVERINFO,
    output_type=_SERVERINFO,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='exit',
    full_name='server_side.P2P.exit',
    index=1,
    containing_service=None,
    input_type=_SERVERINFO,
    output_type=_SERVERINFO,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='join',
    full_name='server_side.P2P.join',
    index=2,
    containing_service=None,
    input_type=_SERVERINFO,
    output_type=_SERVERINFO,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='build_finger_table',
    full_name='server_side.P2P.build_finger_table',
    index=3,
    containing_service=None,
    input_type=_FINGERTABLE,
    output_type=_FINGERTABLE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='notify_cluster',
    full_name='server_side.P2P.notify_cluster',
    index=4,
    containing_service=None,
    input_type=_FINGERTABLE,
    output_type=_VOID,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_P2P)

DESCRIPTOR.services_by_name['P2P'] = _P2P

# @@protoc_insertion_point(module_scope)
