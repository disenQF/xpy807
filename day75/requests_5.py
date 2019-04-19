"""
requests库基于urllib和urllib3, 封装一套网络请求的函数
常用的函数包含：
1） requests.get(url, params, headers, proxies)
2)  requests.post(url, data, json, headers, proxies)
    data 是form表单参数-> content-type= application/x-www-form-urlencode
    json 是上传的json格式的字节流, content-type=application/json

在传参时，params、data、json、headers、proxies都是dict类型

3） 最基本的函数（也是get和post的两函数的"老大",意味最终都调用的是它）
   requests.request(method, url, params, data, json, headers, proxies)
   注意： params, data, json, headers, proxies必须以关键参数传值
"""
import requests


def update(**values):
    url = 'http://10.12.152.218:5000/ip/'  # put方法
    resp = requests.request('PUT', url, data=values)
    print(resp.json())

def delete(ip):
    url = 'http://10.12.152.218:5000/ip/%s/' % ip
    resp = requests.request('DELETE', url)
    print(resp.json())


if __name__ == '__main__':
    # data = {
    #     'ip': '10.12.152.211',
    #     'port': '9876',
    #     'type': 'https',
    #     'source':'https://www.xicidaili.com/nn/'
    # }
    # update(**data)

    delete('10.12.152.211')