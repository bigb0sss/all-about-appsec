#!/usr/bin/python3

import requests
import sys
import jwt

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

    except:
        print("[ERROR] Something went wrong!")
        sys.exit(1)

    return jwt_token

def jwt_handle(jwt_token):

    # Token Parse
    token_head = jwt_token.split(".")[0]
    token_payload = jwt_token.split(".")[1]
    token_secret = jwt_token.split(".")[2]
    

if __name__ == '__main__':
    url = "https://jwt-lab.herokuapp.com"
    endpoint = "/authentication/none"

    username = "bigb0ss"
    password = "password"

    jwt_token = login(url, endpoint, username, password)
    jwt_handle(jwt_token)

