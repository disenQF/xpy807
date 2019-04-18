"""

提取用户的头像和用户名
//div[@class='author clearfix']//img/@src |
//div[@class='author clearfix']//img/@alt

提取简述的内容
//div[@class='content']/span[1]


提取评论或详情的页面连接
//span[@class='stats-comments']/a/@href


提取下一页的连接
//ul[@class='pagination']/li[last()]/a/@href

"""
from urllib.request import Request, urlopen
import csv
import os
import re

import ssl

import time

ssl._create_default_https_context = ssl._create_unverified_context

from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0'
}


def get(url):
    request = Request(url, headers=headers)
    resp = urlopen(request)
    charset = re.findall(r'charset=(\w+)', resp.getheader('Content-Type'))[0]
    html = resp.read()
    parse(html.decode(charset))


def parse(html):
    """
    //div[@class='author clearfix']//img/@src |
    //div[@class='author clearfix']//img/@alt
    """
    root = etree.HTML(html)  # 将html文本转成xpath可提取的element 对象
    author_imgs = root.xpath("//div[@class='author clearfix']//img")  # list[Element, ...]

    # 提供文本内容信息
    # //div[@class='content']/span[1]/text()
    contents = root.xpath("//div[@class='content']/span[1]/text()") # list['', '', '',...]

    for index, img in enumerate(author_imgs):
        # img -> element
        # element的常用方法: get('属性名'), text 标签的文本, xpath()选择子元素的路径
        href = img.get('src')
        name = img.get('alt')
        save(dict(href=href, name=name, content=contents[index]))


    # 提取下一页的连接
    # //ul[@class='pagination']/li[last()]/a/@href

    next_href = root.xpath("//ul[@class='pagination']/li[last()]/a/@href")
    # 如果查询是具体的内容，则返回list中元素不是Element
    print(next_href)  # list['', '' ,.. ]
    time.sleep(3)
    get('https://www.qiushibaike.com'+next_href[0])  # 请求下一个页面

def save(item):
    print(item['name'], item['content'], sep='\n')


if __name__ == '__main__':
    get('https://www.qiushibaike.com/text/')
