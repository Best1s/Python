#-*- coding: utf-8 -*-
import requests
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
headers = {'User-Agent':user_agent}
r = requests.get('http://www.baidu.com',headers=headers)

if r.status_code == requests.codes.ok:
  print r.status_code #响应吗
  print r.headers #响应头  包换所有的响应头
  print r.headers.get('content-type') #推荐使用这种方式
  print r.headers['content-type'] #不推荐
else:
  r.raise_for_status()