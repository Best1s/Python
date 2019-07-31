#coding:utf-8
from multiprocessing.managers import BaseManager
#import Queue
from HtmlDownLoader import HtmlDownLoader
from HtmlParser import HtmlParser
import time
class SpiderWork(object):
  def __init__(self):

    BaseManager.register('get_task_queue')
    BaseManager.register('get_result_queue')

    BaseManager.register('get_task_queue',callable=lambda:url_q)
    BaseManager.register('get_result_queue',callable=lambda:result_q)

    server_addr = '127.0.0.1'
    print 'Connect to server %s...' % server_addr
    self.m = BaseManager(address=(server_addr,8001),authkey='baike')

    self.m.connect()
    self.task = self.m.get_task_queue()
    self.result = self.m.get_result_queue()
    self.downloader = HtmlDownLoader()
    self.parser = HtmlParser()
    print 'init finish'

  def crawl(self):
    while(True):
      try:
        
        if not self.task.empty():
          url = self.task.get()
          if url == 'end':
            print '控制节点通知爬虫节点停止工作...'
            self.result.put({'new_urls':'end','data':'end'})
            return
          print '爬虫节点正在解析：%s' %url.encode('urf-8')
          content = self.downloader.download(url)
          new_urls,data = self.parser.parser(url,content)
          self.result.put({'new_urls':new_urls,'data':data})

      except EOFError,e:
        print 'connect fail!'
        return
      except Exception,e:
        print e
        print 'Crawl fail!'

if __name__ == '__main__':
  spider = SpiderWork()
  spider.crawl()