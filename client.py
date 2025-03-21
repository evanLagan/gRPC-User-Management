import grpc
import user_pb2
import user_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = user_pb2_grpc.UserServiceStub(channel)

        # Register User
        reg_response = stub.RegisterUser(user_pb2.RegisterRequest(username="alice", email="alice@mail.com", password="1234"))
        print(f"Registered User ID: {reg_response.user_id}")

        # Login
        login_response = stub.Login(user_pb2.LoginRequest(username="alice", password="1234"))
        print(f"Login: {login_response.message}, Token: {login_response.token}")

        # Get User Info
        user_response = stub.GetUser(user_pb2.UserRequest(user_id=reg_response.user_id))
        print(f"User Info: {user_response.username}, {user_response.email}")

        # List All Users (Streaming)
        print("Listing All Users:")
        for user in stub.ListUsers(user_pb2.Empty()):
            print(f"ID: {user.user_id}, Username: {user.username}, Email: {user.email}")

if __name__ == '__main__':
    run()
