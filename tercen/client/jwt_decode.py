import sys
sys.path.insert(0, './') # location of src 

import time

from tercen.client.factory import TercenClient
import jwt

username = 'admin'
passw = 'admin'

# Generated for tests from 
encoded_jwt = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3RlcmNlbi5jb20iLCJleHAiOjE3Mzk1MzA0MTAsImRhdGEiOnsiZCI6IiIsInUiOiJhZG1pbiIsImUiOjE3Mzk1MzA0MTA0NzZ9fQ.4fOoCkwMknlXuYDVsf086NjqwQ3pCpvBzOGEtdvxziw"
token_json = jwt.decode(encoded_jwt,  algorithms=["HS256"], options={"verify_signature": False})

client = TercenClient("http://127.0.0.1:5400")
client.userService.connect(username, passw)

token = client.userService.createToken(userId="admin", validityInSeconds=2)

print("CREATED TOKEN")
print(token)

# print(encoded_jwt)

token_json = jwt.decode( token ,  algorithms=["HS256"], options={"verify_signature": False})
print("")
print("DECODING THE TOKEN")
print(token_json)

print(token.split("."))

if client.userService.isTokenValid( token=token):
    print("Token valid")

time.sleep(5)

if not client.userService.isTokenValid( token=token):
    print("Token expired")


