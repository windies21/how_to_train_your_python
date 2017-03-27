from flask import Flask, render_template
import grpc
import train02_pb2_grpc
import train02_pb2

app = Flask(__name__)


@app.route('/')
def home():
    channel = grpc.insecure_channel("localhost:58802")
    stub = train02_pb2_grpc.ListenerStub(channel)

    response = stub.getList(train02_pb2.ListRequest())
    print("items: " + response.items)
    items = response.items.split('|')
    return render_template('home.html', items=items)


@app.route('/add/<username>')
def add(username):
    channel = grpc.insecure_channel("localhost:58802")
    stub = train02_pb2_grpc.ListenerStub(channel)

    response = stub.Listen(train02_pb2.ListenerRequest(request="add", name=username))
    print("Listener received: " + response.message)
    return "Action: " + response.message + "<br />name: " + response.name + "<br />Response: %d" % response.response


@app.route('/del/<username>')
def delete(username):
    channel = grpc.insecure_channel("localhost:58802")
    stub = train02_pb2_grpc.ListenerStub(channel)

    response = stub.Listen(train02_pb2.ListenerRequest(request="del", name=username))
    print("Listener received: " + response.message)
    return "Action: " + response.message + "<br />name: " + response.name + "<br />Response: %d" % response.response


if __name__ == '__main__':
    app.run(debug=True)
