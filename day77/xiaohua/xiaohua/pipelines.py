# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class XiaohuaPipeline(object):
    def __init__(self):
        self.csv_filename = 'xh.csv'
        self.existed_header = False

    def process_item(self, item, spider):
        # item -> dict
        with open(self.csv_filename, 'a') as f:
            writer = csv.DictWriter(f, fieldnames=item.keys())
            if not self.existed_header:
                writer.writeheader()
                self.existed_header = True

            writer.writerow(item)

        return item
