import requests

x = requests.get('https://mail.google.com/mail/u/0/?zx=l7b1ma8xjth9#inbox')
print(type(x))
print(x.status_code)
print(type(x.status_code))
