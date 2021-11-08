#!/usr/bin/python3

import requests
from requests.api import get, head
import json

def post_confirm_transfer(url):
    endpoint = "/confirm_transfer"
    id = "/1"

    headers = {
        'Content-Type': 'application/json',
        'X-API-Token': 'vfuzd2nvaweojqolm4kq',
    }

    r = requests.post(url + endpoint + id, headers=headers)
    print(r.status_code)
    pretty_json = json.loads(r.text)
    print(json.dumps(pretty_json, indent=2))

if __name__ == '__main__':
    url = "http://192.168.2.133:5000"

    post_confirm_transfer(url)