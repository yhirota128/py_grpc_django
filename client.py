import sys
import grpc
from build import helloworld_pb2, helloworld_pb2_grpc

if len(sys.argv) == 1:
    print("usage: python client.py localhost:5000")
    exit()
host = sys.argv[1]
with grpc.insecure_channel(host) as channel:
    stub = helloworld_pb2_grpc.GreeterStub(channel)
    name = input('name>')
    response = stub.SayHello(helloworld_pb2.HelloRequest(name=name))
    print(response.message)
