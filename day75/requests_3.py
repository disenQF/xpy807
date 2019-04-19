import requests

from util import header


def page(p=1, s=5):
    url = 'http://10.12.152.218:5000/query/'
    # 生成查询参数
    params = {
        'page': p,
        's': s
    }
    # resp = requests.get(url, params, headers=header.get_headers())
    query_params = '?'
    for key, val in params.items():
        query_params += "%s=%s&" % (key, val)

    query_params = query_params[:-1]

    resp = requests.get(url + query_params,
                        headers=header.get_headers())

    print(resp.json())


if __name__ == '__main__':
    page(3)
    # page(2)
