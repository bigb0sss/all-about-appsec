import requests

def createDB(url):

    r = requests.get(url + "/createdb")
    print(r.text)

def main():
    url = 'http://172.16.54.128:5000'
    createDB(url)

if __name__ == '__main__':
    main()
