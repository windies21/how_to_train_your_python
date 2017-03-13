"""The Python implementation of the GRPC helloworld.Greeter client."""

import grpc
import sample_pb2
import sample_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = sample_pb2_grpc.TrainerStub(channel)

    response = stub.Train(sample_pb2.TrainRequest(name='Hicup'))
    print("Trainer client received: " + response.message)


if __name__ == '__main__':
    run()
