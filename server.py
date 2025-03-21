import grpc
from concurrent import futures
import user_pb2
import user_pb2_grpc
import users_data
import uuid

class UserServiceServicer(user_pb2_grpc.UserServiceServicer):

    def RegisterUser(self, request, context):
        global users_data
        user_id = users_data.next_id
        users_data.users[user_id] = {
            'username': request.username,
            'email': request.email,
            'password': request.password
        }
        users_data.next_id += 1
        return user_pb2.RegisterReply(user_id=user_id, message="User registered!")

    def GetUser(self, request, context):
        user = users_data.users.get(request.user_id)
        if user:
            return user_pb2.UserReply(user_id=request.user_id, username=user['username'], email=user['email'])
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('User not found!')
            return user_pb2.UserReply()

    def ListUsers(self, request, context):
        for user_id, user in users_data.users.items():
            yield user_pb2.UserReply(user_id=user_id, username=user['username'], email=user['email'])

    def Login(self, request, context):
        for uid, user in users_data.users.items():
            if user['username'] == request.username and user['password'] == request.password:
                token = str(uuid.uuid4())
                users_data.tokens[token] = uid
                return user_pb2.LoginReply(success=True, message="Login successful", token=token)
        return user_pb2.LoginReply(success=False, message="Invalid credentials", token="")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("User Management gRPC Server running on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

        
    