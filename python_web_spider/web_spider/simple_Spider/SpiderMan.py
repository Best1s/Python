#coding: utf-8
from firstSpider.DataOutput import DataOutput
from firstSpider.HtmlDownLoader import HtmlDownLoader
from firstSpider.HtmlParser import HtmlParser
from firstSpider.UrlManager import UrlManager
import time
class SpiderMan(object):
    #进行类的初始化
  def __init__(self):
    self.manager = UrlManager()
    self.downloader = HtmlDownLoader()
    self.parser = HtmlParser()
    self.output = DataOutput()
  def crawl(self,root_url):
    #添加入口url
    self.manager.add_new_url(root_url)
    
    #判断url管理器中是否有新的url,同时判断抓取了多少个url
    while (self.manager.has_new_url() and self.manager.old_url_size() < 20):
      time.sleep(1)
      try:
        #从url管理器中获取新的url
        new_url = self.manager.get_new_url()
        #HTML 下载器下载页面
        html = self.downloader.download(new_url)
        #HTML 解析器抽取页面数据
        new_urls,data = self.parser.parser(new_url,html)
        #将抽取的url 添加到url管理器中
        self.manager.add_new_urls(new_urls)
        #数据存储器存储文件
        self.output.store_data(data)
        print '已经抓取%s个链接' % self.manager.old_url_size()
      except Exception,e:  #Exception	常规错误的基类
        print 'crawl failed'
    #数据存储器将文件输出成指定格式
    self.output.output_html()
if __name__ == '__main__':
    #https://baike.baidu.com/item/5g
    spider_man = SpiderMan()
    spider_man.crawl('http://baike.baidu.com/view/284853.html')
