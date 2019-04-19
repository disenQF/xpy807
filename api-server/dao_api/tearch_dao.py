from dao_api import DB

class TeacherDao:
    def __init__(self):
        self.db = DB()

    def query_all(self):
        sql = 'select * from teacher'
        with self.db as c:
            c.execute(sql)
            result = list(c.fetchall())

        return result

    def save(self, **value):
        sql = 'insert teacher(tn, name) values(%(tn)s, %(name)s)'
        with self.db as c:
            c.execute(sql, args=value)
            if c.rowcount > 0:
                print('添加数据成功', value)
            else:
                print('添加数据失败', value)

    def close(self):
        self.db.close()