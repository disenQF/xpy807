from dao_api import DB


class IPDao:
    def __init__(self):
        self.db = DB()
        self.table_name = 't_ip'

    def save(self, ip, port, type, source):
        existed_sql = 'select table_name from information_schema.tables where table_name=%s'
        create_sql = "create table t_ip(ip varchar(15), " \
                     "port varchar(5)," \
                     "type varchar(5)," \
                     "source varchar(50) )"
        sql = 'insert into t_ip(ip, port, type, source) values(%s, %s, %s, %s)'
        with self.db as c:
            c.execute(existed_sql, args=(self.table_name, ))
            row = c.fetchone()
            if not row:
                c.execute(create_sql) # 执行 DDL语句时，会自动提交事务

            c.execute(sql, args=(ip, port, type, source))
            if c.rowcount > 0:
                print('插入ip成功', (ip, port, type, source))

    def query_all(self):
        with self.db as c:
            c.execute('select * from t_ip')
            result = list(c.fetchall())

        return result

    def update(self, **values):
        # 保证 ip是唯一的
        sql = 'update t_ip set port=%(port)s, type=%(type)s, source=%(source)s where ip=%(ip)s'
        with self.db as c:
            c.execute(sql, args=values)
            if c.rowcount > 0:
                print('更新成功', sql, values)
            else:
                print('更新失败', sql, values)

    def delete(self, ip):
        with self.db as c:
            c.execute('delete from t_ip where ip=%s', args=(ip,))
            if c.rowcount > 0:
                print('删除成功')
            else:
                print('删除失败')