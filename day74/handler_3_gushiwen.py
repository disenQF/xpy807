"""
CookieJar和HTTPCookieProcess处理器的应用
1） login接口，实现登录操作
2） 登录之后，再请求个人中心，获取个人收藏的信息

使用的步骤
1) 创建http.cookiejar.CookieJar 类对象
2) 创建urllib.request.HTTPCookieProcessor对象，并传入CookieJar对象
3）将HTTPCookieProcess对象添加到opener

"""

from http.cookiejar import CookieJar
from urllib.parse import urlencode
from urllib.request import HTTPHandler, HTTPCookieProcessor, build_opener, Request
from urllib.request import urlretrieve

from util import html, header, ydm_api

from lxml import etree
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 让opener具有HTTP请求的能力
# 和Cookie信息的处理能力
opener = build_opener(
    HTTPHandler(),
    HTTPCookieProcessor(CookieJar())
)


def request(url, data: dict, headers=None):
    if data:
        # 将post上传的数据转成字节流
        form_params = urlencode(data)  # key=value&key2=value2
        req = Request(url, form_params.encode(), headers)
    else:
        if headers:
            req = Request(url, headers=headers)
        else:
            req = Request(url)

    resp = opener.open(req)
    html_txt = html.to_html(resp.read(),
                            html.get_charset(resp.getheader('Content-Type')))
    print(html_txt)



if __name__ == '__main__':
    login_url = 'https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx'
    collect_url = 'https://so.gushiwen.org/user/collect.aspx'

    # 验证码的图片
    code_url = 'https://so.gushiwen.org/RandCode.ashx'
    urlretrieve(code_url, 'code.png') # 刷新并保存验证图片

    # 注意： ydm_api模块，需要安装requests库
    # pip install requests
    result = ydm_api.ydm('code.png')
    print('验证码的结果：', result)
    data = {
        'action':'',
        'from':'http://so.gushiwen.org/user/collect.aspx',
        'email': '610039018@qq.com',
        'pwd': 'disen8888',
        'code': result  # 验证码， 第三方平台的API解码
    }

    request(login_url, data, headers=header.get_headers())
    # request(collect_url)


