"""
urlopen() 只负责下载
urlretrieve() 下载并存储到文件中

1） 在请求时，如果添加一个请求头
2） 如果发起post请求
"""
import re
from urllib.request import urlopen, Request


def get(url):
    # 声明请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0',
        'Cookie': '__cfduid=dce29ab8587a6cafa917962eac2dfe2d11555483488; '
                  'Hm_lvt_9b496e3d6adef11b924b6b261a56dff8=1555483491;'
                  ' Hm_lpvt_9b496e3d6adef11b924b6b261a56dff8=1555483514;'
                  ' BDTUJIAID=491cb6336da24c06bd13398fe2e150a6',
        'Referer': 'http://www.baidu.com/'
    }

    # 创建请求，可以添加请求头
    request = Request(url, headers=headers)

    response = urlopen(request)  # 发起请求

    # 判断请求是否成功
    assert response.code == 200  # 如果断言失败，则抛出AssertionError
    print(url, '请求成功!')
    # html = response.read()

    lines = ''
    charset = None
    for line in response:  # 可迭代的response
        if not charset:
            # 尝试从正文中获取字符集
            try:
                line_txt = line.decode()
                lines += line_txt
                if line_txt.startswith('<meta'):
                    s = re.findall(r'charset=(\w+?)"', line_txt)
                    if s:
                        charset = s[0]
            except:
                pass

            continue

        try:
            lines += line.decode(charset)
        except:
            pass

    print(charset)
    print(lines)
    # html = lines.decode(charset)
    # print(html)
    # print(response.getheader('Content-Type'))


if __name__ == '__main__':
    url = 'http://www.haha56.net/'
    get(url)
