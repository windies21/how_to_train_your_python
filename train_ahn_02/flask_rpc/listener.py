import time
import grpc
import train02_pb2 as train
import train02_pb2_grpc as train_grpc
from concurrent import futures


class Listener(train_grpc.ListenerServicer):

    members = []

    def Listen(self, request, context):
        action = request.request.lower()
        member = request.name
        message = ""
        response = 0
        if action == "add":
            """ add member """
            self.members.append(member)
            response = 1
            message = "add member"
        elif action == "del":
            """ delete member """
            if member in self.members:
                message = "remove member"
                response = 1
                self.members.remove(member)
            else:
                message = "failed to remove"
                response = 0

        print(member + " " + message + "response: %d" % response)
        return train.ListenerReply(name=member, response=response, message=message)

    def getList(self, request, context):
        items = '|'.join(self.members)
        print("Send items: " + items)
        return train.ListReply(items=items)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    train_grpc.add_ListenerServicer_to_server(Listener(), server)
    server.add_insecure_port('[::]:58802')
    server.start()
    print("Start Listener server on 58802")

    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        print("\nStop by keyboard interrupt!")
        server.stop(0)

if __name__ == '__main__':
    serve()
