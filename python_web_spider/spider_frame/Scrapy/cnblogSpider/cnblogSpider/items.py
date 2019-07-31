# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnblogspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    content = scrapy.Field()
    cimage_urls = scrapy.Field()
    cimages = scrapy.Field()


'''
#Field用于声明项目的对象不会保留为类属性。相反，可以通过Item.fields属性访问
item = CnblogspiderItem(title='Python 爬虫',content='爬虫开发')
print item['title']
print item.get('title')
item['title']='爬虫'
print item.keys()
print item.items()
#item的复制
item2 = CnblogspiderItem(item)
item3 = item.copy()
dict与item的转化
dict_item = dict(item)
item = CnblogspiderItem({'title':'爬虫','content':'开发'})

#item 扩展 用来添加更多的字段
class newCnblogItem(CnblogspiderItem):
  body = scrapy.Field()
  #也可以使用原字段数据，添加新的值修改原来的值来扩展字段元数据：
class newCnblogItem(CnblogspiderItem):
  title = scrapy.field(CnblogspiderItem.fields['title'],serializer=my_serializer)

'''