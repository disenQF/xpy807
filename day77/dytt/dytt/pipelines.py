# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DyttPipeline(object):
    def __init__(self):
        self.csv_filename = 'dytt.csv'
        self.existed_header = False

    def process_item(self, item, spider):
        # item -> dict对象，是spider.parse() yield {} 输出的结果

        return item
