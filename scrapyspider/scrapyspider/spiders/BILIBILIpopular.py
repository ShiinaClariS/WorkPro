"""

"""
import re
import pandas as pd
import scrapy
from lxml import etree
from scrapyspider.items import BItem
import time
import logging


class BilibiliPopularRankSpider(scrapy.Spider):
    name = 'scrapyspider'
    allowed_domain = []
    url = 'https://www.bilibili.com/v/popular/rank/all'
    url_1 = 'https://www.bilibili.com/v/popular/rank/'
    kind = 'bangumi'
    offset = 0

    start_urls = [url]

    path = list('/html/body/div[3]/div[2]/div[2]/ul/li[%d]' % li for li in range(1, 51))
    insert, update = 0, 0

    def parse(self, response):
        try:
            if response.status != 200:
                return
            for path in self.path:
                item = BItem()
                html = etree.HTML(response.text)
                bvurl = html.xpath(path + '/div[2]/div[1]/a/@href')[0].replace('//', '')
                item['bvurl'] = 'https://' + bvurl
                item['bv'] = item['bvurl'].split('/')[-1]
                item['nowrank'] = html.xpath(path + '/@data-rank')[0]
                item['score'] = html.xpath(path + '/div[2]/div[2]/div[2]/div/text()')[0]

                yield scrapy.Request(item['bvurl'], meta={'meta_1': item}, callback=self.BvPageparse)

            logging.info('新增数据%d条 更新数据%d条', self.insert, self.update)
            self.crawler.engine.close_spider(self)
            # logging.info('爬虫将在两小时后再次启动')
            # time.sleep(7200)
            yield scrapy.Request(self.url, callback=self.parse)
        except Exception as e:
            print(e)

    def BvPageparse(self, response):
        path1 = '/html/body/div[2]/div[4]/div[1]'
        path2 = '/html/body/div[3]/div[1]/div[2]'
        meta_1 = response.meta['meta_1']

        item = BItem()
        item['bvurl'] = meta_1['bvurl']
        item['bv'] = meta_1['bv']
        item['nowrank'] = meta_1['nowrank']
        item['score'] = meta_1['score']
        try:
            if response.status != 200:
                return
            html = etree.HTML(response.text)
            # 标题
            item['title'] = html.xpath(path1 + '/div[1]/h1/span/text()')[0]
            # 播放量
            item['view'] = int(re.findall(r'\d+', html.xpath(path1 + '/div[1]/div/span[1]/@title')[0])[0])
            # 弹幕数
            item['danmu'] = int(re.findall(r'\d+', html.xpath(path1 + '/div[1]/div/span[2]/@title')[0])[0])
            # 投稿日期
            item['contributedate'] = html.xpath(path1 + '/div[1]/div/span[3]/text()')[0]
            # 历史排名
            item['historyrank'] = int(
                re.findall(r'\d+', html.xpath(path1 + '/div[1]/div/span[4]/text()')[0].replace('/xa0', '').strip())[0])
            # 点赞
            item['like'] = int(re.findall(r'\d+', html.xpath(path1 + '/div[3]/div[1]/span[1]/@title')[0])[0])
            # 投币
            item['coin'] = html.xpath(path1 + '/div[3]/div[1]/span[2]/text()')[0].strip()
            # 收藏
            item['collect'] = html.xpath(path1 + '/div[3]/div[1]/span[3]/text()')[0].strip()
            # 分享
            item['share'] = html.xpath(path1 + '/div[3]/div[1]/span[4]/text()')[0].strip()
            # up
            item['up'] = html.xpath("//div[@class='up-info_right']//a[1]/text()")[0].strip()
            # up个人页
            item['upspace'] = 'https:' + html.xpath("//div[@class='up-info_right']//a[1]/@href")[0]
            # 关注
            item['subscribe'] = html.xpath("//span[@class='has-charge']/span/text()")[0]

            yield item

        except Exception as e:
            print(e)
