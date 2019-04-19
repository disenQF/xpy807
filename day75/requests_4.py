import requests


def add_ip(**data):
    url = 'http://10.12.152.218:5000/ip/' # post请求
    resp = requests.post(url, data=data)
    # 响应的数据是json类型
    result = resp.json()
    print(result)

def query_ip():
    url = 'http://10.12.152.218:5000/ip/query/'  # get请求
    resp = requests.get(url)
    result = resp.json()

    print(result)


if __name__ == '__main__':
    # add_ip(ip='119.102.24.141',
    #        port='9999',
    #        type='https',
    #        source='https://www.xicidaili.com/nn')

    query_ip()
