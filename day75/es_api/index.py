"""
对es的索引进行操作,
ElasticSearch使用RESTful规范，数据交互json
1） 创建索引
2)  查询索引
"""

import requests


def add_index(index_name):
    url = 'http://localhost:9200/%s' % index_name
    # 添加索引的请求方法： put

    json = {
        "settings": {
            "number_of_shards": 5,
            "number_of_replicas": 1
        }
    }

    resp = requests.put(url, json=json)
    print(resp.json())

def query(index_name):
    url = 'http://localhost:9200/%s' % index_name
    resp = requests.get(url)
    print(resp.json())

if __name__ == '__main__':
    add_index('stu')
    query('stu')