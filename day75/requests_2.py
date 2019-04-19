import requests

def get_all_teacher():
    # 查询所有的老师, 请求方法是GET
    url = 'http://10.12.152.218:5000/teacher/'
    resp = requests.get(url)

    print(resp.url)
    print(resp.status_code)
    print(resp.headers)
    print('charset=', resp.encoding)
    print(resp.text)
    print(resp.content)
    data = resp.json()
    for item in data:  # data -> list
        # item -> dict
        print(item['name'], item['tn'])


if __name__ == '__main__':
    get_all_teacher()