#-*- coding: utf-8 -*-
import urllib
from lxml import etree
import requests
from time import sleep
import sys
import os
#import pdb

sava_path = sys.path[0] + '/img/'

if os.path.exists(sava_path) == False:
  os.mkdir(sava_path)
'''
urllib模块的 urlretrieve() 方法将远程数据下载到本地
函数原型
urlretrieve(url,filename=None,reporthook=None,data=None)

参数url：下载链接地址
参数filename：指定了保存本地路径（如果参数未指定，urllib会生成一个临时文件保存数据。）
参数reporthook：是一个回调函数，当连接上服务器、以及相应的数据块传输完毕时会触发该回调，我们可以利用这个回调函数来显示当前的下载进度。
参数data：指post导服务器的数据，该方法返回一个包含两个元素的(filename, headers) 元组，filename 表示保存到本地的路径，header表示服务器的响应头

'''
#pdb.set_trace() 

def Schedule(blocknum,blocksize,totalsize):  #回调函数  
  '''
  blocknum:已经下载的数据块
  blocksize:数据块的大小
  totalsize:远程文件的大小
  '''
  per = 100.0 * blocknum * blocksize / totalsize
  if per > 100:
    per = 100
  print 'Download over is: %d' %per

url = 'http://www.ivsky.com/tupian/ziranfengguang/'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
headers = {'User-Agent':user_agent}
r = requests.get(url,headers=headers)
html = etree.HTML(r.text)
img_urls = html.xpath('.//img/@src')  #找到所有的img
i = 0

for img_url in img_urls:
  #print img_url
  img_url = 'http:' + img_url
  #定义图片保存路径
  sava_path = sys.path[0] + '/img/' + 'img' + str(i) + '.jpg'
  sleep(1)
  urllib.urlretrieve(img_url,sava_path,Schedule)
  i += 1