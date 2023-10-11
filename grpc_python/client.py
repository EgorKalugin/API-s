import grpc
import greeting_pb2
import greeting_pb2_grpc


def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = greeting_pb2_grpc.GreetingServiceStub(channel)
    name = input("Enter your name: ")
    request = greeting_pb2.HelloRequest(name=name)
    response = stub.SayHello(request)
    print("Server response:", response.message)


if __name__ == "__main__":
    run()
