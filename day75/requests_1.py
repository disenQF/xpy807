import requests


if __name__ == '__main__':
    url = 'http://10.12.152.218:5000/teacher/'
    data = {
        'tn': '100009',
        'name': 'disen8888888'
    }

    resp = requests.post(url, json=data)
    print(resp.json())