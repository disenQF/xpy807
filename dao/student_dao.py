from dao.base_dao import BaseDao


class StudentDao(BaseDao):
    def query_all(self):
        return self.query('student',
                          'sn', 'name',
                          where=' where sn > %s',
                          args=('03',))


if __name__ == '__main__':
    dao = StudentDao()
    print(dao.query_all())