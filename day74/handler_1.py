"""
使用urllib库中的Handler处理器
1) 处理器需要添加到 opener 浏览器对象中
2）所有的请求(Request)将会由 opener 打开

常用的Handler处理器
1) HTTPHandler 处理http请求
2) CookieJarProcess 处理cookie
3) ProxyHandler   处理代理
"""
import re
from urllib.request import Request, build_opener, HTTPHandler

from util import html
from util.header import get_headers


def request(url):
    # 1. 创建opener对象 - 类似于一个浏览器工具
    opener = build_opener(HTTPHandler())

    # 2. 构建请求对象 Request
    req = Request(url, headers=get_headers())

    # 3. 发起请求
    resp = opener.open(req)
    print(type(resp))  # http.client.HTTPResponse
    if resp.code == 200:
        # print(resp.getheader('Content-Type'))

        charset = html.get_charset(resp.getheader('Content-Type'))

        html_text = html.to_html(resp.read(),charset)
        print(html_text)

def parse(html):
    # 作业1：使用re正则或xpath
    # 提取图片的url和名称
    # 保存到csv文件中
    # 找到下一页的连接，并请求
    pass

if __name__ == '__main__':
    url = 'http://sc.chinaz.com/tupian/shuaigetupian.html'
    request(url)