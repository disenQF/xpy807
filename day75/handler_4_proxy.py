"""
处理IP代理处理器 urllib.request.ProxyHandler
1) 处理器一定与opener一块使用, urllib.request.build_opener()
2) ProxyHandler也可以和HTTPHandler、HTTPCookieProcessor一起组合使用
3）ProxyHandler创建时，需要提供一个proxies 参数
   - proxies给定是一个字典对象， 如
   {'http': '10.11.11.90:8776',
    'https': '98.12.11.12:80' }
"""
import re
from urllib.request import build_opener, HTTPHandler, ProxyHandler, Request

from util import header
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def get(url, proxies):
    opener = build_opener(HTTPHandler(),
                          ProxyHandler(proxies))
    resp = opener.open(Request(url, headers=header.get_headers()))
    if resp.code == 200:
        print('--请求成功--')
        html = resp.read()
        html_text = html.decode()
        s = re.findall(r"<a href='/ipv4/\d+\.\d+\.\d+\.\d+'>(\d+\.\d+\.\d+\.\d+)</a>", html_text)

        print('当前主机的IP: ', s)


if __name__ == '__main__':
    # 从免费的IP代理网站获取代理的ip、port、类型(http/https)
    proxies = {
        # 'HTTPS': '119.102.24.141:9999'
        'HTTP': '119.102.29.228:9999'
    }
    get('https://zh-hans.ipshu.com/my_info', proxies)