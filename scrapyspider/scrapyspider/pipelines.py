# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
import logging
from scrapyspider.spiders import BILIBILIpopular


class ScrapyspiderPipeline:
    def process_item(self, item, spider):
        return item


class SaveToMongodbPipeline(object):

    def __init__(self):
        client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
        db = client['BilibiliRankDB']
        self.cluster = db['BInfo']

    def process_item(self, item, spider):
        try:
            item['_id'] = item['bv']
            if self.cluster.count_documents({'_id': item['_id']}) != 0:
                logging.info(item['bv'] + '当前bv已存在，将进行更新')
                self.cluster.update({'_id': item['id']}, {'$set': {dict(item)}})
                # self.update += 1
                BILIBILIpopular.BilibiliPopularRankSpider.update += 1
            else:
                self.cluster.insert(dict(item))
                logging.info(item['bv'] + '已新增该bv')
                # self.insert += 1
                BILIBILIpopular.BilibiliPopularRankSpider.insert += 1
        except Exception as e:
            print(e)
        # logging.info('新增数据%d条\n更新数据%d条', self.insert, self.update)


# class CountDataPipeline(object):
#     insert, update = 0, 0
#
#     def __init__(self):
#         self.insert, self.update = SaveToMongodbPipeline.insert, SaveToMongodbPipeline.update
#
#     def process_item(self, item, spider):
#         logging.info('新增数据%d条 更新数据%d条', self.insert, self.update)

# class TestPipeline:
#     def process_item(self, item):
#         print(item)
