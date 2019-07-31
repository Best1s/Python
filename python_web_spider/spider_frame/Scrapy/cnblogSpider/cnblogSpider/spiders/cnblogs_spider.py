#coding:utf-8
import scrapy
#from cnblogSpider.items import CnblogspiderItem
from ..items import CnblogspiderItem

class CnblogsSpider(scrapy.Spider):
  name = 'cnblogs'  #爬虫名字
  allowed_domains = ['cnblogs.com'] #允许的域名
  start_urls = ['http://www.cnblogs.com/qiyeboy/default.html?page=1']
  #start_urls = ['http://www.baidu.com']
  def parse(self,response):
    # 实现网页的解析  
    #response.xpath(".//*[@class='postTitle']/a/text()").extract()
  
    papers = response.xpath(".//*[@class='day']")

    for paper in papers:
      url = paper.xpath(".//*[@class='postTitle']/a/@href").extract()[0]
      title = paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]
      time = paper.xpath(".//*[@class='dayTitle']/a/text()").extract()[0]
      content = paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]
      #print url,title,time,content
      #item = CnblogsSpider(url=url,title=title,time=time,content=content)
      item = CnblogspiderItem(url=url,title=title,time=time,content=content)
      request = scrapy.Request(url=url,callback=self.parse_body)
      request.meta['item'] = item
      yield request
      #用 yield 关键字提交item,将parse 方法打造成一个生成器
      #yield item
      
    #翻页功能
    #next_page = Selector(response).re(u'<a href="(\S*)">下一页</a>')
    next_pages = response.xpath(".//*[@class='topicListFooter']")
    for next_page in next_pages:
      next_page = next_page.xpath("//a").re(u'<a href="(\S*)">下一页</a>')
      if next_page:
        yield scrapy.Request(url=next_page[0],callback=self.parse)

  def parse_body(self,response):
    item = response.meta['item']
    body = response.xpath(".//*[@class='postBody']")
    item['cimage_urls'] = body.xpath('.//img//@src').extract()
    yield item
  
if __name__=='__main__':
  process = CrawlerProcess({
    'USER_AGENT':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
  })
  process.crawl(CnblogsSpider)
  process.start()