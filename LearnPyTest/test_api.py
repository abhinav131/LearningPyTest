import pytest
import json
import requests
import logging

#logger = logging.getLogger(__name__)
#logger = logging.getLogger(__name__)

# def main_url():
#     return "https://reqres.in/"

def test_valid_login1():
    url = "https://reqres.in/api/login"
    #data = {'email': 'awe@wed.com', 'password': 'qwerty'}
    data = {'email':'eve.holt@reqres.in', 'password': 'cityslicka' }
    response = requests.post(url, data=data)
    #try:
    print(type(response))
    token = json.loads(response.text)
    assert response.status_code == 200
    assert token['token'] == "QpwL5tke4Pnpja7X4"
    #assert True
   # except Exception as e:
        #logging.error(f"Mail has not been send due to: {e}")

# def test_valid_login2():
#     url = "https://reqres.in/api/login"
#     data = {'email': 'eve.holt@reqres.in', 'password': 'qwert@y'}
#     response = requests.post(url, data=data)
#     print((response.status_code))
#     token = json.loads(response.text)
#     assert response.status_code == 200
#     assert token['token'] == "QpwL5tke4Pnpja7X4"
#
# def test_valid_login3():
#     url = "https://reqres.in/api/login"
#     data = {'email': 'awe@wed.com', 'password': 'cityslicka'}
#     response = requests.post(url, data=data)
#     print((response.status_code))
#     token = json.loads(response.text)
#     assert response.status_code == 200
#     assert token['token'] == "QpwL5tke4Pnpja7X4"
#     assertFalse()
#
# def test_valid_login4():
#     url = "https://reqres.in/api/login"
#     data = {'email': 'awe@wed.com', 'password': 'qwerty'}
#     response = requests.post(url, data=data)
#     print((response.status_code))
#     token = json.loads(response.text)
#     assert response.status_code == 200
#     assert token['token'] == "QpwL5tke4Pnpja7X4"
#
# def test_valid_login5():
#     url = "https://reqres.in/api/login"
#     data = {'email': '', 'password': 'qwerty'}
#     response = requests.post(url, data=data)
#     print((response.status_code))
#     token = json.loads(response.text)
#     assert response.status_code == 200
#     assert token['token'] == "QpwL5tke4Pnpja7X4"
#
# def test_valid_login6():
#     url = "https://reqres.in/api/login"
#     data = {'email': '', 'password': 'qwerty'}
#     response = requests.post(url, data=data)
#     print((response.status_code))
#     token = json.loads(response.text)
#     assert response.status_code == 200
#     assert token['token'] == "QpwL5tke4Pnpja7X4"
#
# def test_valid_login7():
#     url = "https://reqres.in/api/login"
#     data = {'email': 'eve.holt@reqres.in', 'password': ''}
#     response = requests.post(url, data=data)
#     print((response.status_code))
#     token = json.loads(response.text)
#     assert response.status_code == 200
#     assert token['token'] == "QpwL5tke4Pnpja7X4"
#
# def test_valid_login8():
#         url = "https://reqres.in/api/login"
#         data = {'email': 'awe@wed.com', 'password': ''}
#         response = requests.post(url, data=data)
#         print((response.status_code))
#         token = json.loads(response.text)
#         assert response.status_code == 200
#         assert token['token'] == "QpwL5tke4Pnpja7X4"
#
#
# def test_valid_login9():
#     url = "https://reqres.in/api/login"
#     data = {'email': '', 'password': ''}
#     response = requests.post(url, data=data)
#     print((response.status_code))
#     token = json.loads(response.text)
#     assert response.status_code == 200
#     assert token['token'] == "QpwL5tke4Pnpja7X4"
