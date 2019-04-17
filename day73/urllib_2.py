"""
urlopen() 只负责下载
urlretrieve() 下载并存储到文件中

1） 在请求时，如果添加一个请求头
2） 如果发起post请求
"""
import json
import re
from urllib.request import urlopen, Request
from urllib.parse import quote, urlencode

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

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

def post(url, data, headers):
    # 实现post请求 + 请求头
    # 设置Request的data参数时，就是post请求
    # data是字节码
    data = urlencode(data) # 生成form表单的参数编码，application/x-www-form-urlencoded
    request = Request(url, data.encode('utf-8'), headers)

    # 发起请求
    resp = urlopen(request)
    if resp.code == 200:
        # 响应的数据是json类型
        resp_data = resp.read()

        # 获取字符集
        content_type = resp.getheader('Content-Type')
        s = re.findall(r'charset=(\w+)', content_type)
        if s:
            charset = s[0]
            json_data = resp_data.decode(charset)
        else:
            json_data = resp_data.decode()

        print(json_data)
        means = json.loads(json_data)
        print(means.get('dict_result').get('simple_means').get('word_means'))


if __name__ == '__main__':
    # url = 'http://www.haha56.net/'
    # get(url)

    url = 'https://fanyi.baidu.com/v2transapi'
    data = {
        'from': 'en',
        'to': 'zh',
        'query': 'apple',
        'transtype': 'realtime',
        'simple_means_flag': '3',
        'sign': '704513.926512',
        'token': '9fc86fc625f77e503a53653963384464'
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0',
        'Cookie': 'BAIDUID=C54A17B138600A57FB71E5003D727C91:FG=1; BIDUPSID=C54A17B138600A57FB71E5003D727C91; PSTM=1545292520; BDUSS=J1UzR4TFNVUFZOd3p3OHd4VmxBME1UbGM5V29CRVNIWkQ0N3phVzItUXJFYnRjQVFBQUFBJCQAAAAAAAAAAAEAAACVZ8A3ZGF2aWVfYW5kcm9pZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACuEk1wrhJNccm; H_PS_PSSID=1445_21094_28774_28723_28557_28831_28585_26350_28604; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; cflag=13%3A3; BDRCVFR[gltLrB7qNCt]=mk3SLVN4HKm; BDRCVFR[Fc9oatPmwxn]=srT4swvGNE6uzdhUL68mv3; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1555488376; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1555488376; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1'
    }

    post(url, data, headers)


