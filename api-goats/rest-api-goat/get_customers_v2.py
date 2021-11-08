#!/usr/bin/python3

import requests
from requests.api import get, head

# [GET] get_customer_v2
def get_customer_v2(url):
    endpoint = "/get_customer_v2"
    user_id = "/2"

    headers = {
        'Content-Type': 'application/json',
        'X-API-Token': 'vfuzd2nvaweojqolm4kq',
    }

    r = requests.get(url+endpoint+user_id, headers=headers)
    print(r.status_code)
    print(r.text)


if __name__ == '__main__':
    url = "http://192.168.2.133:5000"

    get_customer_v2(url)