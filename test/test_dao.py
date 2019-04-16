"""
通过单元测试，测试DB类是否能正常使用
"""

from unittest import TestCase

from dao import DB

class TestDao(TestCase):
    def test_conn(self):
        db = DB()
        # 断言成功后，程序会继续运行
        # 如果断言失败，则会中断程序运行
        self.assertIsNotNone(db.conn, '连接数据库失败')

    def test_query(self):
        db = DB()
        with db as c:
            sql = """
            select table_name, table_type from information_schema.tables
            where table_schema=%s
            """
            c.execute(sql, args=('stu1',))
            for row in c.fetchall():
                print(row)

    def test_insert(self):
        db = DB()

        # 进入上下文时，调用db的__enter__()函数，将函数返回的对象赋给了c
        # 退出上下文时，调用db的__exit__(except_type, except_val, except_tb)
        with db as c:
            sql = 'insert student(sn, name,age, sex) ' \
                  'values( %(sn)s, %(name)s, %(age)s,  %(sex)s )'
            stu = {
                'sn': 10009,
                'name': 'disen',
                'age': '1999-10-10',
                'sex': '男'
            }
            c.execute(sql, args=stu)
            self.assertGreater(c.rowcount, 0, '插入失败')

    def test_query1(self):
        """
        作业1：查询01课程成绩大于02课程成绩的学生姓名、两门课程的成绩
        """
        pass