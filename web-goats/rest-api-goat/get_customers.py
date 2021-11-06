#!/usr/bin/python3

import requests
from requests.api import get, head

# [GET] get_customers
def get_customers(url):
    endpoint = "/get_customers"

    headers = {
        'Content-Type': 'application/json',
        'X-API-Token': 'vfuzd2nvaweojqolm4kq',
    }

    r = requests.get(url+endpoint, headers=headers)
    print(r.status_code)
    print(r.text)

if __name__ == '__main__':
    url = "http://192.168.2.133:5000"

    get_customers(url)