#-*- condig: utf-8 -*-
'''import requests
r = requests.get('http://www.baidu.com')
print(chardet.detect(r.content))
r.encoding = chardet.detect(r.content)['encoding']
'''

import requests
r = requests.get('http://www.baidu.com',stream=True)  #stream=True  以字节流方式读取
print r.raw.read(10)  #指定去读字节数

