from grpc_tools import protoc

protoc.main((
    '',
    '-I./protos',
    '--python_out=./grpcDefinitions',
    '--grpc_python_out=./grpcDefinitions',
    './protos/sd_work.proto',
))
protoc.main((
    '',
    '-I./protos',
    '--python_out=./grpcDefinitions',
    '--grpc_python_out=./grpcDefinitions',
    './protos/server_side.proto',
))
