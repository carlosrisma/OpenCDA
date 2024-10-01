# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: carla.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x63\x61rla.proto\x12\x05\x63\x61rla\x1a\x1bgoogle/protobuf/empty.proto\"\x1b\n\x08\x41\x63torIds\x12\x0f\n\x07\x61\x63torId\x18\x01 \x03(\x05\"\x15\n\x06Number\x12\x0b\n\x03num\x18\x01 \x01(\x05\"\x81\x02\n\x07Vehicle\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x1c\n\x05speed\x18\x02 \x01(\x0b\x32\r.carla.Vector\x12#\n\x0c\x61\x63\x63\x65leration\x18\x03 \x01(\x0b\x32\r.carla.Vector\x12\x1f\n\x08location\x18\x04 \x01(\x0b\x32\r.carla.Vector\x12\x10\n\x08latitude\x18\x05 \x01(\x01\x12\x11\n\tlongitude\x18\x06 \x01(\x01\x12\x0e\n\x06length\x18\x07 \x01(\x01\x12\r\n\x05width\x18\x08 \x01(\x01\x12\x0c\n\x04lane\x18\t \x01(\x05\x12\x0f\n\x07heading\x18\n \x01(\x01\x12#\n\ttransform\x18\x0b \x01(\x0b\x32\x10.carla.Transform\")\n\x06Vector\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\"4\n\x08Rotation\x12\r\n\x05pitch\x18\x01 \x01(\x01\x12\x0b\n\x03yaw\x18\x02 \x01(\x01\x12\x0c\n\x04roll\x18\x03 \x01(\x01\"O\n\tTransform\x12\x1f\n\x08location\x18\x01 \x01(\x0b\x32\r.carla.Vector\x12!\n\x08rotation\x18\x02 \x01(\x0b\x32\x0f.carla.Rotation\"\xb0\x02\n\x06Object\x12\n\n\x02id\x18\x01 \x01(\x05\x12\n\n\x02\x64x\x18\x02 \x01(\x01\x12\n\n\x02\x64y\x18\x03 \x01(\x01\x12\x1c\n\x05speed\x18\x04 \x01(\x0b\x32\r.carla.Vector\x12#\n\x0c\x61\x63\x63\x65leration\x18\x05 \x01(\x0b\x32\r.carla.Vector\x12\x0e\n\x06length\x18\x06 \x01(\x01\x12\r\n\x05width\x18\x07 \x01(\x01\x12\x0f\n\x07onSight\x18\x08 \x01(\x08\x12\x0f\n\x07tracked\x18\t \x01(\x08\x12\x11\n\ttimestamp\x18\n \x01(\x05\x12\x12\n\nconfidence\x18\x0b \x01(\x01\x12\x0b\n\x03yaw\x18\x0c \x01(\x01\x12#\n\ttransform\x18\r \x01(\x0b\x32\x10.carla.Transform\x12\x10\n\x08\x64\x65tected\x18\x0e \x01(\x08\x12\x13\n\x0bperceivedBy\x18\x0f \x01(\x05\")\n\x07Objects\x12\x1e\n\x07objects\x18\x01 \x03(\x0b\x32\r.carla.Object\"\x18\n\x07\x42oolean\x12\r\n\x05value\x18\x01 \x01(\x08\"M\n\tObjectsIn\x12!\n\ncpmObjects\x18\x01 \x03(\x0b\x32\r.carla.Object\x12\r\n\x05\x65goId\x18\x02 \x01(\x05\x12\x0e\n\x06\x66romId\x18\x03 \x01(\x05\"H\n\x08ObjectIn\x12\x1d\n\x06object\x18\x01 \x01(\x0b\x32\r.carla.Object\x12\r\n\x05\x65goId\x18\x02 \x01(\x05\x12\x0e\n\x06\x66romId\x18\x03 \x01(\x05\"[\n\x07\x43ontrol\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x1f\n\x08waypoint\x18\x02 \x01(\x0b\x32\r.carla.Vector\x12\r\n\x05speed\x18\x03 \x01(\x01\x12\x14\n\x0c\x61\x63\x63\x65leration\x18\x04 \x01(\x01\"\xd7\x01\n\x08Waypoint\x12\x1f\n\x08location\x18\x02 \x01(\x0b\x32\r.carla.Vector\x12!\n\x08rotation\x18\x03 \x01(\x0b\x32\x0f.carla.Rotation\x12\x0f\n\x07road_id\x18\x04 \x01(\x05\x12\x12\n\nsection_id\x18\x05 \x01(\x05\x12\x13\n\x0bis_junction\x18\x06 \x01(\x08\x12\x13\n\x0bjunction_id\x18\x07 \x01(\x05\x12\x0f\n\x07lane_id\x18\x08 \x01(\x05\x12\x12\n\nlane_width\x18\t \x01(\x01\x12\x13\n\x0blane_change\x18\n \x01(\x05\"_\n\rObjectMinimal\x12\n\n\x02id\x18\x01 \x01(\x05\x12#\n\ttransform\x18\x02 \x01(\x0b\x32\x10.carla.Transform\x12\x0e\n\x06length\x18\x03 \x01(\x01\x12\r\n\x05width\x18\x04 \x01(\x01\"\x1c\n\x0b\x44oubleValue\x12\r\n\x05value\x18\x01 \x01(\x01\x32\xcd\x07\n\x0c\x43\x61rlaAdapter\x12<\n\x12\x45xecuteOneTimeStep\x12\x16.google.protobuf.Empty\x1a\x0e.carla.Boolean\x12\x38\n\x06\x46inish\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\x12>\n\x13GetManagedActorsIds\x12\x16.google.protobuf.Empty\x1a\x0f.carla.ActorIds\x12<\n\x11GetManagedCAVsIds\x12\x16.google.protobuf.Empty\x1a\x0f.carla.ActorIds\x12\x34\n\x13GetManagedActorById\x12\r.carla.Number\x1a\x0e.carla.Vehicle\x12.\n\rInsertVehicle\x12\x0e.carla.Vehicle\x1a\r.carla.Number\x12?\n\x13GetRandomSpawnPoint\x12\x16.google.protobuf.Empty\x1a\x10.carla.Transform\x12,\n\x0bGetActorLDM\x12\r.carla.Number\x1a\x0e.carla.Objects\x12.\n\x0cInsertObject\x12\x0f.carla.ObjectIn\x1a\r.carla.Number\x12\x35\n\rInsertObjects\x12\x10.carla.ObjectsIn\x1a\x12.carla.DoubleValue\x12/\n\x08InsertCV\x12\x0f.carla.ObjectIn\x1a\x12.carla.DoubleValue\x12,\n\x0cGetCartesian\x12\r.carla.Vector\x1a\r.carla.Vector\x12&\n\x06GetGeo\x12\r.carla.Vector\x1a\r.carla.Vector\x12\'\n\x06hasLDM\x12\r.carla.Number\x1a\x0e.carla.Boolean\x12\x34\n\nSetControl\x12\x0e.carla.Control\x1a\x16.google.protobuf.Empty\x12\x32\n\x10GetCarlaWaypoint\x12\r.carla.Vector\x1a\x0f.carla.Waypoint\x12\x36\n\x14GetNextCarlaWaypoint\x12\r.carla.Vector\x1a\x0f.carla.Waypoint\x12\x39\n\rGetGTaccuracy\x12\x14.carla.ObjectMinimal\x1a\x12.carla.DoubleValueb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'carla_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ACTORIDS']._serialized_start=51
  _globals['_ACTORIDS']._serialized_end=78
  _globals['_NUMBER']._serialized_start=80
  _globals['_NUMBER']._serialized_end=101
  _globals['_VEHICLE']._serialized_start=104
  _globals['_VEHICLE']._serialized_end=361
  _globals['_VECTOR']._serialized_start=363
  _globals['_VECTOR']._serialized_end=404
  _globals['_ROTATION']._serialized_start=406
  _globals['_ROTATION']._serialized_end=458
  _globals['_TRANSFORM']._serialized_start=460
  _globals['_TRANSFORM']._serialized_end=539
  _globals['_OBJECT']._serialized_start=542
  _globals['_OBJECT']._serialized_end=846
  _globals['_OBJECTS']._serialized_start=848
  _globals['_OBJECTS']._serialized_end=889
  _globals['_BOOLEAN']._serialized_start=891
  _globals['_BOOLEAN']._serialized_end=915
  _globals['_OBJECTSIN']._serialized_start=917
  _globals['_OBJECTSIN']._serialized_end=994
  _globals['_OBJECTIN']._serialized_start=996
  _globals['_OBJECTIN']._serialized_end=1068
  _globals['_CONTROL']._serialized_start=1070
  _globals['_CONTROL']._serialized_end=1161
  _globals['_WAYPOINT']._serialized_start=1164
  _globals['_WAYPOINT']._serialized_end=1379
  _globals['_OBJECTMINIMAL']._serialized_start=1381
  _globals['_OBJECTMINIMAL']._serialized_end=1476
  _globals['_DOUBLEVALUE']._serialized_start=1478
  _globals['_DOUBLEVALUE']._serialized_end=1506
  _globals['_CARLAADAPTER']._serialized_start=1509
  _globals['_CARLAADAPTER']._serialized_end=2482
# @@protoc_insertion_point(module_scope)
