"""
使用urllib下载网页
1) urllib.request.urlopen() 打开网页
2) urllib.request.urlretrieve()  下载网页到文件中
3）response 响应对象
    - code/status 响应状态码
    - headers/info 请求头
    - read() 响应的字节数据
    - readline()/readlines() 响应的文本的数据
"""
from http.client import HTTPResponse
from threading import Thread
from urllib.request import urlopen, urlretrieve

# 解决ssl证书的问题
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

from util.md5_format import md5_code


def download(url):
    # 下载（请求）url
    # 如果data参数不为空，则表示本次请求的方法是POST,反之为GET
    response: HTTPResponse = urlopen(url)
    if response.getcode() == 200:
        print(response.geturl(), '--请求成功---')
        # print(response.info())  # 响应头(原始的header信息)
        print(type(response.headers))
        print(type(response))
        print(response.status, response.code, response.getcode())
        print(type(response.headers),  # http.client.HTTPMessage
              type(response.info()),  # http.client.HTTPMessage
              type(response.getheaders()))  # list((key, value), ....)
        print(response.getheaders())
        print(response.getheader('Content-Type'))  # 读取响应头的key
        print(response.getheader('Content-Length'))  # 不存在的key,返回None

        # html = response.readlines()  # 读取所有的网页信息
        # 读取响应文本数据的字符集
        content_type = response.getheader('Content-Type')  # text/html; charset=utf-8
        charset = content_type.split(';')[-1].split('=')[-1]

        html = response.read().decode(encoding=charset)
        print(html)

        with open('gushiwen.html', mode='w', encoding=charset) as file:
            file.write(html)
    else:
        print(response.geturl(), '请求失败', response.code)


def save_url(url, filename):
    # 下载并保存网页
    urlretrieve(url, filename)


def save_img(url):
    if url.endswith('.jpg') or url.endswith('.png'):
        urlretrieve(url, url.split('/')[-1])
        return

    filename = md5_code(url)
    resp = urlopen(url)

    # 读取响应的图片类型 jpg, png, gif
    content_type = resp.getheader('Content-Type')
    img_type = content_type.split(';')[0]
    if img_type == 'image/png':
        filename += '.png'
    elif img_type == 'image/gif':
        filename += '.gif'
    else:
        filename += '.jpg'

    with open(filename, mode='wb') as file:
        file.write(resp.read())

    print('保存图片%s 成功' % filename)


def async_download(url):
    Thread(target=save_img, args=(url, )).start()


if __name__ == '__main__':
    # download('https://www.gushiwen.org/')
    # save_url('https://www.gushiwen.org/', '1.html')
    # save_img('https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=678166707,880764255&fm=179&app=42&f=JPEG?w=121&h=140')
    url1 = 'https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=678166707,880764255&fm=179&app=42&f=JPEG?w=121&h=140'
    async_download(url1)
    print('--开始下载图片--', url1)