# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import carla_pb2 as carla__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class CarlaAdapterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ExecuteOneTimeStep = channel.unary_unary(
                '/carla.CarlaAdapter/ExecuteOneTimeStep',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Finish = channel.unary_unary(
                '/carla.CarlaAdapter/Finish',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetManagedActorsIds = channel.unary_unary(
                '/carla.CarlaAdapter/GetManagedActorsIds',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=carla__pb2.ActorIds.FromString,
                )
        self.GetManagedActorById = channel.unary_unary(
                '/carla.CarlaAdapter/GetManagedActorById',
                request_serializer=carla__pb2.Number.SerializeToString,
                response_deserializer=carla__pb2.Vehicle.FromString,
                )
        self.InsertVehicle = channel.unary_unary(
                '/carla.CarlaAdapter/InsertVehicle',
                request_serializer=carla__pb2.Vehicle.SerializeToString,
                response_deserializer=carla__pb2.Number.FromString,
                )
        self.GetRandomSpawnPoint = channel.unary_unary(
                '/carla.CarlaAdapter/GetRandomSpawnPoint',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=carla__pb2.Transform.FromString,
                )
        self.GetActorLDM = channel.unary_unary(
                '/carla.CarlaAdapter/GetActorLDM',
                request_serializer=carla__pb2.Number.SerializeToString,
                response_deserializer=carla__pb2.Objects.FromString,
                )
        self.InsertObject = channel.unary_unary(
                '/carla.CarlaAdapter/InsertObject',
                request_serializer=carla__pb2.ObjectIn.SerializeToString,
                response_deserializer=carla__pb2.Number.FromString,
                )
        self.GetCartesian = channel.unary_unary(
                '/carla.CarlaAdapter/GetCartesian',
                request_serializer=carla__pb2.Vector.SerializeToString,
                response_deserializer=carla__pb2.Vector.FromString,
                )
        self.GetGeo = channel.unary_unary(
                '/carla.CarlaAdapter/GetGeo',
                request_serializer=carla__pb2.Vector.SerializeToString,
                response_deserializer=carla__pb2.Vector.FromString,
                )
        self.hasLDM = channel.unary_unary(
                '/carla.CarlaAdapter/hasLDM',
                request_serializer=carla__pb2.Number.SerializeToString,
                response_deserializer=carla__pb2.Boolean.FromString,
                )


class CarlaAdapterServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ExecuteOneTimeStep(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Finish(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetManagedActorsIds(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetManagedActorById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InsertVehicle(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRandomSpawnPoint(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetActorLDM(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InsertObject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCartesian(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetGeo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def hasLDM(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CarlaAdapterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ExecuteOneTimeStep': grpc.unary_unary_rpc_method_handler(
                    servicer.ExecuteOneTimeStep,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Finish': grpc.unary_unary_rpc_method_handler(
                    servicer.Finish,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetManagedActorsIds': grpc.unary_unary_rpc_method_handler(
                    servicer.GetManagedActorsIds,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=carla__pb2.ActorIds.SerializeToString,
            ),
            'GetManagedActorById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetManagedActorById,
                    request_deserializer=carla__pb2.Number.FromString,
                    response_serializer=carla__pb2.Vehicle.SerializeToString,
            ),
            'InsertVehicle': grpc.unary_unary_rpc_method_handler(
                    servicer.InsertVehicle,
                    request_deserializer=carla__pb2.Vehicle.FromString,
                    response_serializer=carla__pb2.Number.SerializeToString,
            ),
            'GetRandomSpawnPoint': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRandomSpawnPoint,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=carla__pb2.Transform.SerializeToString,
            ),
            'GetActorLDM': grpc.unary_unary_rpc_method_handler(
                    servicer.GetActorLDM,
                    request_deserializer=carla__pb2.Number.FromString,
                    response_serializer=carla__pb2.Objects.SerializeToString,
            ),
            'InsertObject': grpc.unary_unary_rpc_method_handler(
                    servicer.InsertObject,
                    request_deserializer=carla__pb2.ObjectIn.FromString,
                    response_serializer=carla__pb2.Number.SerializeToString,
            ),
            'GetCartesian': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCartesian,
                    request_deserializer=carla__pb2.Vector.FromString,
                    response_serializer=carla__pb2.Vector.SerializeToString,
            ),
            'GetGeo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGeo,
                    request_deserializer=carla__pb2.Vector.FromString,
                    response_serializer=carla__pb2.Vector.SerializeToString,
            ),
            'hasLDM': grpc.unary_unary_rpc_method_handler(
                    servicer.hasLDM,
                    request_deserializer=carla__pb2.Number.FromString,
                    response_serializer=carla__pb2.Boolean.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'carla.CarlaAdapter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CarlaAdapter(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ExecuteOneTimeStep(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/carla.CarlaAdapter/ExecuteOneTimeStep',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Finish(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/carla.CarlaAdapter/Finish',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetManagedActorsIds(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/carla.CarlaAdapter/GetManagedActorsIds',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            carla__pb2.ActorIds.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetManagedActorById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/carla.CarlaAdapter/GetManagedActorById',
            carla__pb2.Number.SerializeToString,
            carla__pb2.Vehicle.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InsertVehicle(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/carla.CarlaAdapter/InsertVehicle',
            carla__pb2.Vehicle.SerializeToString,
            carla__pb2.Number.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRandomSpawnPoint(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/carla.CarlaAdapter/GetRandomSpawnPoint',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            carla__pb2.Transform.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetActorLDM(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/carla.CarlaAdapter/GetActorLDM',
            carla__pb2.Number.SerializeToString,
            carla__pb2.Objects.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InsertObject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/carla.CarlaAdapter/InsertObject',
            carla__pb2.ObjectIn.SerializeToString,
            carla__pb2.Number.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCartesian(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/carla.CarlaAdapter/GetCartesian',
            carla__pb2.Vector.SerializeToString,
            carla__pb2.Vector.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetGeo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/carla.CarlaAdapter/GetGeo',
            carla__pb2.Vector.SerializeToString,
            carla__pb2.Vector.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def hasLDM(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/carla.CarlaAdapter/hasLDM',
            carla__pb2.Number.SerializeToString,
            carla__pb2.Boolean.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
