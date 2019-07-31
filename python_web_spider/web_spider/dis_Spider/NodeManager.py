#coding:utf-8
from multiprocessing.managers import BaseManager
from UrlManager import UrlManager
from DataOutput import DataOutput
import time
#import NodeManager
#url_q：url管理进程将url传递给爬虫节点的通道
#result_q：爬虫节点返回数据给数据提取的通道
#conn_q：数据提取进程，将新的url数据提交给url管道的进程通信
#store_q： 是数据提取进程，将过去的数据交给数据存储进程的通信
class NodeManager(object):

  def start_Manager(self,url_q, result_q):

    #把创建的两个队列注册在网络上，利用register方法，callable参数关联Queue对象，将Queue对象在网络中暴露
    BaseManager.register('get_task_queue',callable=lambda:url_q)
    BaseManager.register('get_result_queue',callable=lambda:result_q)

    #绑定端口8001 设置口令 'baike'  相当于对象的初始化
    manager = BaseManager(address=('127.0.0.1',8001),authkey='baike')
    return manager

  def url_manager_proc(self,url_q,conn_q,root_url):
    url_manager = UrlManager()
    url_manager.add_new_url(root_url)
    n = 0
    while True:
   
      while(url_manager.has_new_url()):

        new_url = url_manager.get_new_url()
        url_q.put(new_url)
        print 'old_url =',url_manager.old_url_size()

        if (url_manager.old_url_size() > 100):
          url_q.put('end')
          print '控制节点发起节点结束通知'
          url_manager.save_progress('new_urls.txt',url_manager.new_urls)
          url_manager.save_progress('old_urls.txt',UrlManager.old_urls)
          return
      try:
        if not conn_q.empty():
          urls = conn_q.get()
          url_manager.add_new_urls(urls)
          url_manager.add_new_urls(urls)
      except BaseException,e:
        time.sleep(0.1)

  def result_solve_proc(self,result_q,conn_q,store_q):
    while(True):
      try:
        if not result_q.empty():
          content = result_q.get(True)
          if content('new_urls') == 'end':
            print '分析结果进程接收通知然后结束！'
            store_q.put('end')
            return
          conn_q.put(content['new_urls'])
          store_q.put(content['data'])
        else:
          time.sleep(0.1)
      except BaseException,e:
        time.sleep(0.1)

  def store_proc(self,store_q):
    output = DataOutput()
    while True:
      if not store_q.empty():
        if data == 'end':
          print '存储进程接收通知然后结束'
          output.output_end(output.filepath)
          return
        output.store_data(data)
      else:
        time.sleep(0.1)
