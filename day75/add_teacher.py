import json
from urllib.request import Request, urlopen

# 新增一名新的讲师
# 接口： http://10.12.152.218:5000/teacher/
# 请求方法： POST
# 请求数据格式： json
# 请求数据的样本
# {"tn": "12000", "name": "disen"}

# 返回数据的样本: 略
# 接口符合RESTful规范的，详细有四条：
# 1）每一个资源都有它的唯一标识，称之为URI
# 2) 每一个资源的请求都是无状态的，即为短连接，与Connection: keep-alive 是相对立的。
# 3）每一个资源都有四个标准的动作, GET/POST/PUT/DELETE
# 4) 资源的数据格式都是以json或xml 传输


def json_post(url:str, data:dict):
    json_str = json.dumps(data)
    json_bytes = json_str.encode('utf-8')
    headers = {
        'Content-Type': 'application/json;charset=utf-8',
        'Content-Length': len(json_bytes)
    }
    req = Request(url, data=json_bytes, headers=headers)
    resp = urlopen(req)
    json_ = resp.read().decode()
    return json.loads(json_)


if __name__ == '__main__':
    url = 'http://10.12.152.218:5000/teacher/'
    data = {
        'tn': '100001',
        'name': 'disen'
    }
    resp_data = json_post(url, data)
    print(resp_data)