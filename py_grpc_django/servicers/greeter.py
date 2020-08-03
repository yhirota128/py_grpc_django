from build import helloworld_pb2, helloworld_pb2_grpc


def init(server):
    helloworld_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)


class GreeterServicer(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        response = helloworld_pb2.HelloReply(message="Hello, {}!".format(request.name))
        return response
