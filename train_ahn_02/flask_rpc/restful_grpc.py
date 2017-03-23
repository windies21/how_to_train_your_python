from flask import Flask
from flask_restful import Api, Resource
import grpc
import train02_pb2_grpc
import train02_pb2

app = Flask(__name__)
api = Api(app)


class ListenerGetList(Resource):
    def post(self):
        """ return user list """
        channel = grpc.insecure_channel("localhost:58802")
        stub = train02_pb2_grpc.ListenerStub(channel)

        response = stub.getList(train02_pb2.ListRequest())
        items = response.items.split('|')
        return {"users": items, "response": 1} if items else {"users": [], "response": 0}


class ListenerAddUser(Resource):
    def post(self, username):
        """ add user """
        channel = grpc.insecure_channel("localhost:58802")
        stub = train02_pb2_grpc.ListenerStub(channel)

        response = stub.Listen(train02_pb2.ListenerRequest(request="add", name=username))
        return {"message": response.message, "name": response.name, "response": response.response}


class ListenerDelUser(Resource):
    def post(self, username):
        """ delete user """
        channel = grpc.insecure_channel("localhost:58802")
        stub = train02_pb2_grpc.ListenerStub(channel)

        response = stub.Listen(train02_pb2.ListenerRequest(request="del", name=username))
        return {"message": response.message, "name": response.name, "response": response.response}


class ListenerNoUser(Resource):
    def post(self):
        return {"message": "username required.", "response": 0}

api.add_resource(ListenerGetList, '/')
api.add_resource(ListenerAddUser, '/add/<username>')
api.add_resource(ListenerDelUser, '/del/<username>')
api.add_resource(ListenerNoUser, '/add', '/del', '/add/', '/del/')


if __name__ == '__main__':
    app.run(debug=True)
