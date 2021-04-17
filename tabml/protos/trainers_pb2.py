# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tabml/protos/trainers.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tabml/protos/trainers.proto',
  package='tabml.protos',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1btabml/protos/trainers.proto\x12\x0ctabml.protos\"`\n\x11TrainerLgbmParams\x12\x0f\n\x07verbose\x18\x01 \x01(\x08\x12\x1d\n\x15\x65\x61rly_stopping_rounds\x18\x02 \x01(\x05\x12\x1b\n\x13\x63\x61tegorical_feature\x18\x03 \x03(\t\"F\n\x14TrainerXgboostParams\x12\x0f\n\x07verbose\x18\x01 \x01(\x08\x12\x1d\n\x15\x65\x61rly_stopping_rounds\x18\x02 \x01(\x05\"-\n\x14TrainerSklearnParams\x12\x15\n\rsample_weight\x18\x01 \x01(\x02\"\xf4\x01\n\x07Trainer\x12\x10\n\x08\x63ls_name\x18\x01 \x02(\t\x12\x19\n\ntrain_full\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x36\n\x0blgbm_params\x18\x03 \x01(\x0b\x32\x1f.tabml.protos.TrainerLgbmParamsH\x00\x12<\n\x0exgboost_params\x18\x04 \x01(\x0b\x32\".tabml.protos.TrainerXgboostParamsH\x00\x12<\n\x0esklearn_params\x18\x05 \x01(\x0b\x32\".tabml.protos.TrainerSklearnParamsH\x00\x42\x08\n\x06params'
)




_TRAINERLGBMPARAMS = _descriptor.Descriptor(
  name='TrainerLgbmParams',
  full_name='tabml.protos.TrainerLgbmParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='verbose', full_name='tabml.protos.TrainerLgbmParams.verbose', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='early_stopping_rounds', full_name='tabml.protos.TrainerLgbmParams.early_stopping_rounds', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='categorical_feature', full_name='tabml.protos.TrainerLgbmParams.categorical_feature', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=141,
)


_TRAINERXGBOOSTPARAMS = _descriptor.Descriptor(
  name='TrainerXgboostParams',
  full_name='tabml.protos.TrainerXgboostParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='verbose', full_name='tabml.protos.TrainerXgboostParams.verbose', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='early_stopping_rounds', full_name='tabml.protos.TrainerXgboostParams.early_stopping_rounds', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=143,
  serialized_end=213,
)


_TRAINERSKLEARNPARAMS = _descriptor.Descriptor(
  name='TrainerSklearnParams',
  full_name='tabml.protos.TrainerSklearnParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sample_weight', full_name='tabml.protos.TrainerSklearnParams.sample_weight', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=215,
  serialized_end=260,
)


_TRAINER = _descriptor.Descriptor(
  name='Trainer',
  full_name='tabml.protos.Trainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cls_name', full_name='tabml.protos.Trainer.cls_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='train_full', full_name='tabml.protos.Trainer.train_full', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lgbm_params', full_name='tabml.protos.Trainer.lgbm_params', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='xgboost_params', full_name='tabml.protos.Trainer.xgboost_params', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sklearn_params', full_name='tabml.protos.Trainer.sklearn_params', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='params', full_name='tabml.protos.Trainer.params',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=263,
  serialized_end=507,
)

_TRAINER.fields_by_name['lgbm_params'].message_type = _TRAINERLGBMPARAMS
_TRAINER.fields_by_name['xgboost_params'].message_type = _TRAINERXGBOOSTPARAMS
_TRAINER.fields_by_name['sklearn_params'].message_type = _TRAINERSKLEARNPARAMS
_TRAINER.oneofs_by_name['params'].fields.append(
  _TRAINER.fields_by_name['lgbm_params'])
_TRAINER.fields_by_name['lgbm_params'].containing_oneof = _TRAINER.oneofs_by_name['params']
_TRAINER.oneofs_by_name['params'].fields.append(
  _TRAINER.fields_by_name['xgboost_params'])
_TRAINER.fields_by_name['xgboost_params'].containing_oneof = _TRAINER.oneofs_by_name['params']
_TRAINER.oneofs_by_name['params'].fields.append(
  _TRAINER.fields_by_name['sklearn_params'])
_TRAINER.fields_by_name['sklearn_params'].containing_oneof = _TRAINER.oneofs_by_name['params']
DESCRIPTOR.message_types_by_name['TrainerLgbmParams'] = _TRAINERLGBMPARAMS
DESCRIPTOR.message_types_by_name['TrainerXgboostParams'] = _TRAINERXGBOOSTPARAMS
DESCRIPTOR.message_types_by_name['TrainerSklearnParams'] = _TRAINERSKLEARNPARAMS
DESCRIPTOR.message_types_by_name['Trainer'] = _TRAINER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TrainerLgbmParams = _reflection.GeneratedProtocolMessageType('TrainerLgbmParams', (_message.Message,), {
  'DESCRIPTOR' : _TRAINERLGBMPARAMS,
  '__module__' : 'tabml.protos.trainers_pb2'
  # @@protoc_insertion_point(class_scope:tabml.protos.TrainerLgbmParams)
  })
_sym_db.RegisterMessage(TrainerLgbmParams)

TrainerXgboostParams = _reflection.GeneratedProtocolMessageType('TrainerXgboostParams', (_message.Message,), {
  'DESCRIPTOR' : _TRAINERXGBOOSTPARAMS,
  '__module__' : 'tabml.protos.trainers_pb2'
  # @@protoc_insertion_point(class_scope:tabml.protos.TrainerXgboostParams)
  })
_sym_db.RegisterMessage(TrainerXgboostParams)

TrainerSklearnParams = _reflection.GeneratedProtocolMessageType('TrainerSklearnParams', (_message.Message,), {
  'DESCRIPTOR' : _TRAINERSKLEARNPARAMS,
  '__module__' : 'tabml.protos.trainers_pb2'
  # @@protoc_insertion_point(class_scope:tabml.protos.TrainerSklearnParams)
  })
_sym_db.RegisterMessage(TrainerSklearnParams)

Trainer = _reflection.GeneratedProtocolMessageType('Trainer', (_message.Message,), {
  'DESCRIPTOR' : _TRAINER,
  '__module__' : 'tabml.protos.trainers_pb2'
  # @@protoc_insertion_point(class_scope:tabml.protos.Trainer)
  })
_sym_db.RegisterMessage(Trainer)


# @@protoc_insertion_point(module_scope)
