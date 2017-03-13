"""The Python implementation of the GRPC helloworld.Greeter server."""

import time
import grpc
from concurrent import futures
import sample_pb2
import sample_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Trainer(sample_pb2_grpc.TrainerServicer):

    def Train(self, request, context):
        print("I got Train Request from %s" % request.name)
        return sample_pb2.TrainReply(message='leann, test, run %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sample_pb2_grpc.add_TrainerServicer_to_server(Trainer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Start Trainer Server....")

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        print("\nStop by Keyboard Interrupt!")
        server.stop(0)


if __name__ == '__main__':
    serve()
