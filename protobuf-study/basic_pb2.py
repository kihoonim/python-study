# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: basic.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='basic.proto',
  package='basic_package',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0b\x62\x61sic.proto\x12\rbasic_package\"Y\n\x07Messag1\x12\x0e\n\x06value1\x18\x01 \x01(\x08\x12\x0e\n\x06value2\x18\x02 \x01(\t\x12\x0e\n\x06value3\x18\x03 \x01(\x05\x12\x0e\n\x06value4\x18\x04 \x01(\x03\x12\x0e\n\x06value5\x18\x05 \x01(\x02\x62\x06proto3'
)




_MESSAG1 = _descriptor.Descriptor(
  name='Messag1',
  full_name='basic_package.Messag1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value1', full_name='basic_package.Messag1.value1', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value2', full_name='basic_package.Messag1.value2', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value3', full_name='basic_package.Messag1.value3', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value4', full_name='basic_package.Messag1.value4', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value5', full_name='basic_package.Messag1.value5', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=30,
  serialized_end=119,
)

DESCRIPTOR.message_types_by_name['Messag1'] = _MESSAG1
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Messag1 = _reflection.GeneratedProtocolMessageType('Messag1', (_message.Message,), {
  'DESCRIPTOR' : _MESSAG1,
  '__module__' : 'basic_pb2'
  # @@protoc_insertion_point(class_scope:basic_package.Messag1)
  })
_sym_db.RegisterMessage(Messag1)


# @@protoc_insertion_point(module_scope)
