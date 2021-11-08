#!/usr/bin/python3

import requests
from requests.api import get, head

def connect(url):
    r = requests.get(url)
    print(r.status_code)
    print(r.text)


if __name__ == '__main__':
    url = "http://192.168.2.133:5000"

    connect(url)
