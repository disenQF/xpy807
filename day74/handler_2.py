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

from util import html, header

from lxml import etree

# 让opener具有HTTP请求的能力
# 和Cookie信息的处理能力
opener = build_opener(
    HTTPHandler(),
    HTTPCookieProcessor(CookieJar())
)


def request(url, data: dict, headers: dict):
    # 将post上传的数据转成字节流
    form_params = urlencode(data)  # key=value&key2=value2
    req = Request(url, form_params.encode(), headers)

    # 登录
    resp = opener.open(req)

def get(url, headers):

    resp = opener.open(Request(url, headers=headers))
    html_text = html.to_html(resp.read(),
                             html.get_charset(resp.getheader('Content-Type')))

    root = etree.HTML(html_text)
    account = root.xpath('//p[@class="pt5"]/span/text()')[0]
    print(account)

if __name__ == '__main__':
    login_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=20182122180'
    info_url = 'http://www.renren.com/224549540/profile'

    data = {
        'rkey': '1c7df63368df7ce73c234de26178ec11',
        'password': '19870115',
        'origURL': 'http://www.renren.com/home',
        'key_id': '1',
        'icode': '',
        'f': 'http://www.renren.com/224549540',
        'email': 'dqsygcz@126.com',
        'domain': 'renren.com',
        'captcha_type': 'web_login',
    }

    # request(login_url, data, headers=header.get_headers())
    # headers请求中已经包含了当前url站点的登录后的Cookie信息
    # 可以收集多个账号登录之后的Cookie信息，作为Cookie池
    get('http://user.sc.chinaz.com/index.aspx', headers=header.get_headers())

