import json
from redis import Redis

def load(json_filename):
    with open(json_filename, 'r') as f:
        city_json = json.load(f)  # 加载.json文件，转成dict字典对象
        print(city_json.get('data').get('cityList'))


def save_redis(code, name):  # redis 使用hash类型
    pass


if __name__ == '__main__':
    # load('city.json')
    l = [{'name': 'disen', 'age': 20}, {'name':'jack', 'age':19}]
    # 将l列表写入到l.json文件的中
    with open('l.json', 'w') as f:
        json.dump(l, f)
