import requests
from requests.packages import urllib3
urllib3.disable_warnings()
postdata = {'username':'admin','password':'admin'}
r = requests.post('https://vdazrk-8080-cgkrvy.dev.ide.live/',data=postdata,verify=False)
'''eg:
r = requests.put('https://xxxxxx.com/put',data={'key':'vlue'}) 
r = requests.delete('https://xxxxxx.com/delete')
r = requests.head('https://xxxxxx.com/get')
r = requests.options('https://xxxxxx.com/get')'''

'''add value  eg: http://www.xxxx.com/s/blogpost?Keyword=blog:qiyeboy&pageubdex=1
payload = {'Keywords':'blog:qiyeboy','pageindex':1}
r = requests.get('http://wwwxxxx.com/s/blogpost',params=payload)'''

print r.status_code
print r.content