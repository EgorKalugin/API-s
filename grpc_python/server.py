import grpc
import greeting_pb2
import greeting_pb2_grpc
from concurrent.futures import ThreadPoolExecutor


class GreetingServicer(greeting_pb2_grpc.GreetingServiceServicer):
    def SayHello(self, request, context):
        name = request.name
        message = f"Hello, {name}!"
        return greeting_pb2.HelloResponse(message=message)


def serve():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    greeting_pb2_grpc.add_GreetingServiceServicer_to_server(GreetingServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started listening on port 50051...")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
