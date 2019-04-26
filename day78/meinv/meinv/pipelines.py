# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from meinv import settings

from hashlib import sha1


class MeinvPipeline(object):
    def process_item(self, item, spider):
        return item


class MvImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for url in item['image_urls']:
            yield Request(url, meta={'name': item['name']})

    def item_completed(self, results, item, info):
        # 将下载完成后的图片路径设置到item中
        print(results)
        item['images'] = [x for ok, x in results if ok]
        return item

    def file_path(self, request, response=None, info=None):
        # 为每位人员创建一个目录，存放她自己的所有图片
        author_name = request.meta['name']
        author_dir = os.path.join(settings.IMAGES_STORE, author_name)
        if not os.path.exists(author_dir):
            os.makedirs(author_dir)

        # 生成一个文件名，md5/sha1
        try:
            ext_name = request.url.split('/')[-1].split('.')[-1]
        except:
            ext_name = 'jpg'
        filename = sha1(request.url.encode(encoding='utf-8')).hexdigest()

        # 返回相对IMAGE_STORE的图片路径
        return '%s/%s.%s' % (author_name, filename, ext_name)
