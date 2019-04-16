"""
Database Access Object
"""
import pymysql
from pymysql.cursors import DictCursor

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'stu1',
    'charset': 'utf8'
}

class DB:
    def __init__(self):
        self.conn = pymysql.connect(**config)
        print('--connect ok--')

    def __enter__(self):
        # 进入上下文时，需要返回一个cursor对象
        return self.conn.cursor(cursor=DictCursor)

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 判断是否正常的方式退出上下文
        if not exc_type:
            # 如果是正常情况，则提交事务
            self.conn.commit()
        else:
            # 如果非正常，则回滚事务
            self.conn.rollback()

    def close(self):
        self.conn.close()
