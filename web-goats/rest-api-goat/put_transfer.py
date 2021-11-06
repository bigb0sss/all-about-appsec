#!/usr/bin/python3

import requests
from requests.api import get, head
import json

def transfer(url):

    endpoint = "/transfer"
    
    headers = {
        'Content-Type': 'application/json',
        'X-API-Token': 'vfuzd2nvaweojqolm4kq',
    }

    data = {
        'from': '5',
        'to': '3',
        'ammount': "-500",
    }

    r = requests.put(url + endpoint, data=json.dumps(data), headers=headers)
    print(r.headers)
    print(r.status_code)
    print(r.text)

if __name__ == '__main__':
    url = "http://192.168.2.133:5000"

    transfer(url)
