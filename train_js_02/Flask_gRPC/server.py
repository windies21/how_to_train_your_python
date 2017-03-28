"""The Python implementation of the GRPC Posting server."""

import time
import grpc
from concurrent import futures
import sample_pb2
import sample_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Poster(sample_pb2_grpc.PosterServicer):

    post_list = []

    def AddPost(self, request, context):
        self.post_list.append(request.post)
        print('Add post')
        return sample_pb2.PostReply(message='New entry was successfully posted')

    def GetPosts(self, request, context):
        print('Called GetPosts!!!')
        for post in self.post_list:
            yield post


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sample_pb2_grpc.add_PosterServicer_to_server(Poster(), server)
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
