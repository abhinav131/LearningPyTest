from django.http import HttpRequest
request = HttpRequest()
#
# def request_data():
#     request = HttpRequest()
#     request.data = {}
#     request.data["mobile"] = +918560061197
#     request.data["otp"] = 2345
#     request.data["email"] = "abhinav.modi+thor1@e2enetworks.com"
#     request.data["otpemail"] = 4567
#     return request
#
# x = request_data()
# print(x.get("otp"))

def set_request_data(request, correct_otp):
    # request.data = {}
    request.data["otp"] = correct_otp

set_request_data(23,45)


set_request_data(request, 45)

