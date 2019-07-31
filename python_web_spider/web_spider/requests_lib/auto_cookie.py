#-*- coding: utf-8 -*-
import requests
loginUrl = 'http://www.xxxx.com/login'
s = requests.Session() 
#allow_redirects允许重定向  如果允许 可通过 r.history 字段查看历史信息
r = s.get(loginUrl,allow_redirects=True)  #首先访问界面   获取服务器分配的cookie   
datas={'name':'qiye','passwd':'qiye'}
r = s.post(loginUrl,data=datas,allow_redirects=True)  #发送post请求，
print r.text