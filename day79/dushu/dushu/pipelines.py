# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from pymysql.cursors import DictCursor

from dushu import settings


class DushuPipeline(object):
    def __init__(self):
        # **dict -> 将dict转成关键参数传值格式，如key1=value,key2=value
        self.conn = pymysql.Connect(**settings.DB_CONFIG)
        self.init_db()

        self.batch_count = 0

    def init_db(self):
        with self.conn.cursor(cursor=DictCursor) as c:
            c.execute('drop table if exists t_book')
            sql = """
            create table t_book(id integer PRIMARY key auto_increment,
            name varchar(50), 
            author VARCHAR(50),
            price FLOAT ,
            publisher VARCHAR(200),
            isbn VARCHAR(30), publish_date DATE )
            """
            c.execute(sql)

    def process_item(self, item, spider):
        with self.conn.cursor(cursor=DictCursor) as c:
            sql = 'insert t_book(name,author,price,publisher,publish_date,isbn) ' \
                  'values(%(name)s, %(author)s, %(price)s, %(publisher)s, %(publish_date)s,  %(isbn)s)'

            c.execute(sql, args=item)

        self.batch_count += 1
        if self.batch_count % 100 == 0:
            self.conn.commit()  # 100条数据，批量提交一次

        return item
