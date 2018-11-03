# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import sd_work_pb2 as sd__work__pb2


class ServerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.create = channel.unary_unary(
        '/sd_work.Server/create',
        request_serializer=sd__work__pb2.Data.SerializeToString,
        response_deserializer=sd__work__pb2.ServerResponse.FromString,
        )
    self.read = channel.unary_unary(
        '/sd_work.Server/read',
        request_serializer=sd__work__pb2.Id.SerializeToString,
        response_deserializer=sd__work__pb2.ServerResponse.FromString,
        )
    self.update = channel.unary_unary(
        '/sd_work.Server/update',
        request_serializer=sd__work__pb2.Data.SerializeToString,
        response_deserializer=sd__work__pb2.ServerResponse.FromString,
        )
    self.delete = channel.unary_unary(
        '/sd_work.Server/delete',
        request_serializer=sd__work__pb2.Id.SerializeToString,
        response_deserializer=sd__work__pb2.ServerResponse.FromString,
        )


class ServerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def create(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def read(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def update(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def delete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ServerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'create': grpc.unary_unary_rpc_method_handler(
          servicer.create,
          request_deserializer=sd__work__pb2.Data.FromString,
          response_serializer=sd__work__pb2.ServerResponse.SerializeToString,
      ),
      'read': grpc.unary_unary_rpc_method_handler(
          servicer.read,
          request_deserializer=sd__work__pb2.Id.FromString,
          response_serializer=sd__work__pb2.ServerResponse.SerializeToString,
      ),
      'update': grpc.unary_unary_rpc_method_handler(
          servicer.update,
          request_deserializer=sd__work__pb2.Data.FromString,
          response_serializer=sd__work__pb2.ServerResponse.SerializeToString,
      ),
      'delete': grpc.unary_unary_rpc_method_handler(
          servicer.delete,
          request_deserializer=sd__work__pb2.Id.FromString,
          response_serializer=sd__work__pb2.ServerResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'sd_work.Server', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))