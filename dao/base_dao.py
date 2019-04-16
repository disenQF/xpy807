from dao import DB


class BaseDao():
    def __init__(self):
        self.db = DB()

    def query(self, table_name, *columns, where=None, args=None):

        sql = "select %s from %s" %(','.join(columns), table_name)
        if where:
            sql += where

        with self.db as c:
            c.execute(sql, args=args)
            result = list(c.fetchall())

        return result

    def save(self, table_name, **values):
        pass

    def update(self, table_name, **values):
        pass

    def delete_by_id(self, table_name, id_):
        pass
