from concurrent import futures
import time

import grpc

import basic_pb2
import basic_pb2_grpc


class BasicService(basic_pb2_grpc.BasicServiceServicer):

    def Function1(self, request, context):
        print(request.value)
        return basic_pb2.Reply(value=request.value)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    basic_pb2_grpc.add_BasicServiceServicer_to_server(BasicService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

    print('start')

    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
