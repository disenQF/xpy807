"""
爬取 糗事百科中文字内容及作者信息
url = 'https://www.qiushibaike.com/text/'
1） 下载网页
2） 解析网页，提供作者名和头像的url
3)  将提供的作者名和头像的url存储到csv文件中
"""
import csv
import re
from urllib.request import urlopen, Request
import ssl

import os

ssl._create_default_https_context = ssl._create_unverified_context

def get(url):
    request = Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0'
    })
    resp = urlopen(request)
    print(resp.code, )
    charset = re.findall(r'charset=(\w+)',
                         resp.getheader('Content-Type'))[0]
    html = resp.read()
    html = html.decode(charset)
    parse(html)

def parse(html):
    # 提取用户信息相关的标签 <img src='', alt=''>
    # <img src="//pic.qiushibaike.com/system/avtnew/2621/26217894/thumb/20190415174800.jpg?imageView2/1/w/90/h/90"
    #      alt="聊天不撩妹子">
    base_url = '//pic.qiushibaike.com/system/avtnew/'
    s = re.findall(r'<img src="//pic.qiushibaike.com/system/avtnew/(.+?)" alt="(.+?)">',
                   html)
    for img_url, name in s:
        save({'img_url': 'https:'+base_url+img_url, 'name': name})

def save(item):
    exist_header = os.path.exists('qiushibaike_author.csv')
    with open('qiushibaike_author.csv', 'a') as f:
        writer = csv.DictWriter(f, fieldnames=('name', 'img_url'))
        if not exist_header:
            # 如果文件不存在，则表示第一次写入
            writer.writeheader()

        writer.writerow(item)

    download_img(item.get('img_url'))


def download_img(url):
    # 作业4： 下载图片
    # 要求： 文件名必须是md5的32位长度的字符串，必须带扩展名
    pass


if __name__ == '__main__':
    url = 'https://www.qiushibaike.com/text/'
    get(url)