#!/usr/bin/python3

import requests
import sys
from bs4 import BeautifulSoup

def register(url, endpoint_newUser, endpoint_users):

    # Getting authenticity_token (It's like a CSRF)
    s = requests.session()
    r = s.get(url + endpoint_newUser)
    p = BeautifulSoup(r.content, "lxml")
    auth_token = p.find(attrs = {'name' : 'authenticity_token'})['value']

    username = "bigb0ss1"
    password = "password"

    data = {
        'authenticity_token' : auth_token,
        'user[name]' : username,
        'user[email]' : "email@hello",
        'user[secret_fact]': "email@hello",
        'user[password]': password,
        'user[password_confirmation]': password,
        'commit': "Create+my+account",
    }

    r = s.post(url + endpoint_users, data=data)
    # print(r.status_code)
    # print(r.text)

    if r.status_code == 200:
        print(f"[INFO] New user {username} successfully created!")
    else:
        print("[ERROR] Something went wrong!")
        sys.exit(1)

if __name__ == '__main__':
    url = "https://jwt-lab.herokuapp.com"
    endpoint_newUser = "/users/new"
    endpoint_users = "/users"

    register(url, endpoint_newUser, endpoint_users)
