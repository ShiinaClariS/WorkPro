# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 综合得分
    score = scrapy.Field()
    # 视频链接
    bvurl = scrapy.Field()
    # BV号
    bv = scrapy.Field()
    # up主
    up = scrapy.Field()
    # up主个人页
    upspace = scrapy.Field()
    # 播放量
    view = scrapy.Field()
    # 弹幕数
    danmu = scrapy.Field()
    # 排名
    # rank = scrapy.Field()
    # 点赞
    like = scrapy.Field()
    # 投币
    coin = scrapy.Field()
    # 收藏
    collect = scrapy.Field()
    # 分享
    share = scrapy.Field()
    # 投稿日期
    contributedate = scrapy.Field()
    # 历史排名
    historyrank = scrapy.Field()
    # 当前排名
    nowrank = scrapy.Field()
    # 关注
    subscribe = scrapy.Field()
    #
    _id = scrapy.Field()
