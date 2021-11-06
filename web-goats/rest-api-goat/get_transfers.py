#!/usr/bin/python3

import requests
from requests.api import get, head
import json

def get_transfers(url):
    endpoint = "/get_transfers"

    headers = {
        'Content-Type': 'application/json',
        'X-API-Token': 'vfuzd2nvaweojqolm4kq',
    }

    r = requests.get(url+endpoint, headers=headers)
    print(r.status_code)
    pretty_json = json.loads(r.text)
    print(json.dumps(pretty_json, indent=2))

if __name__ == '__main__':
    url = "http://192.168.2.133:5000"

    get_transfers(url)