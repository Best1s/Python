#-*- coding: utf-8 -*-
import requests
import logging
logging.captureWarnings(True)   #移除ssl私密认证
r = requests.get('https://vdazrk-8080-cgkrvy.dev.ide.live/',verify=False)  #verify=False 关闭ssl认证
print r.content