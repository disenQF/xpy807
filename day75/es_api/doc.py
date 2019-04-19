"""
向teacher索引库中添加文档（一条记录）数据
"""
import requests

def add_doc(type_name, doc_id=None, **doc):
    if doc_id:
        url = 'http://localhost:9200/stu/teacher/%s' % doc_id
    else:
        url = 'http://localhost:9200/stu/teacher'

    resp = requests.post(url, json=doc)
    print(resp.json())

def update_doc(type_name, doc_id=None, **doc):
    url = 'http://localhost:9200/stu/teacher/%s' % doc_id
    resp = requests.put(url, json=doc)
    print(resp.json())


def get(doc_id):
    url = 'http://localhost:9200/stu/teacher/%s' % doc_id
    resp = requests.get(url)
    print(resp.json())

if __name__ == '__main__':
    doc_id = 'AWo1ELLFFMwWShvNxUej'
    # doc_data = {
    #     'tn': '1002',
    #     'name': 'disen'
    # }
    # update_doc('teacher',doc_id=doc_id, **doc_data)

    get(doc_id)