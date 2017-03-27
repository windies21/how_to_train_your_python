from flask import Flask
from flask_restful import Api, Resource
import grpc
import train02_pb2_grpc
import train02_pb2


def connect(host, port):
    channel = grpc.insecure_channel("{0}:{1}".format(host, port))
    stub = train02_pb2_grpc.ListenerStub(channel)
    return stub


class FlaskServiceSampler:
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)

        self.api.add_resource(self.ListenerGetList, '/')
        self.api.add_resource(self.ListenerAddUser, '/add/<username>')
        self.api.add_resource(self.ListenerDelUser, '/del/<username>')
        self.api.add_resource(self.ListenerNoUser, '/add', '/del', '/add/', '/del/')

    def run(self):
        self.app.run(debug=True)

    class ListenerGetList(Resource):
        def get(self):
            """ return user list """
            stub = connect("localhost", "58802")

            response = stub.getList(train02_pb2.ListRequest())
            items = response.items.split('|')
            return {"users": items, "response": 1} if len(items) > 0 else {"users": [], "response": 0}

    class ListenerAddUser(Resource):
        def get(self, username):
            """ add user """
            stub = connect("localhost", "58802")

            response = stub.Listen(train02_pb2.ListenerRequest(request="add", name=username))
            return {"message": response.message, "name": response.name, "response": response.response}

    class ListenerDelUser(Resource):
        def get(self, username):
            """ delete user """
            stub = connect("localhost", "58802")

            response = stub.Listen(train02_pb2.ListenerRequest(request="del", name=username))
            return {"message": response.message, "name": response.name, "response": response.response}

    class ListenerNoUser(Resource):
        def post(self):
            return {"message": "username required.", "response": 0}


if __name__ == '__main__':
    service = FlaskServiceSampler()
    service.run()
