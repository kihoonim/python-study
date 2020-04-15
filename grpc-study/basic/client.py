import grpc

import basic_pb2
import basic_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = basic_pb2_grpc.BasicServiceStub(channel)
        reply = stub.Function1(basic_pb2.Request(value='hello'))
    print(reply.value)


if __name__ == '__main__':
    run()
