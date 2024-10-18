from flask import Blueprint

hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.get("/")
def say_hello_world():
    print("Running say_hello_world")
    return "Hello, World!"













# @hello_world_bp.get("/hello/JSON/")
# def say_hello_moun():
#     return {
#         "name": "Anh Tran",
#         "message": "Hello!",
#         "hobbies": ["Hiking", "Yoga", "Spending time with family"]
#     }
    
# # @hello_world_bp.get("/broken-endpoint-with-broken-server-code/")
# # def broken_endpoint():
# #     response_body = {
# #         "name": "Anh Tran",
# #         "message": "Hello!",
# #         "hobbies": ["Hiking", "Yoga", "Spending time with family"]
# #     }
# #     new_hobby = ["Surfing"]
# #     response_body["hobbies"] = response_body["hobbies"] + new_hobby
# #     return response_body


# # @hello_world_bp.get("/app/routes/") #define path of request
# # def endpoint_name():#execute whenever a request that matches the decorator is received
# #     my_beautiful_response_body = "Hello, World!"
# #     return my_beautiful_response_body