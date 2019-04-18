"""
提取用户信息、内容所在的父Element标签

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
    # 将html文本传入到xpath解析器中
    root = etree.HTML(html)

    # 1. 提取每个用户的区域(共有49个区域)
    articles = root.xpath("//div[starts-with(@class, 'article')]") # list[Element,...]
    for article in articles:
        # 读取作者的头像和姓名
        author = article.xpath("./div[starts-with(@class, 'author')]//img")
        if author:
            name = author[0].get('alt')
            img_url = author[0].get('src')

            # 读取作者发布的内容
            content = article.xpath(".//div[@class='content']/span[1]/text()")

            save(dict(img_url=img_url,
                      name=name,
                      content=content))

def save(item):
    # 去掉content中的\n
    content = item['content'] # list['', '',]
    content = ''.join(content)
    content = content.replace('\n', '')
    print(item['name']+":", content+'\n'+'-'*20, sep='\n')


if __name__ == '__main__':
    get('https://www.qiushibaike.com/text/')
