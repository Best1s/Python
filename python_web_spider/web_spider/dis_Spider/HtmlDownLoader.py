#coding:utf-8
import requests

class HtmlDownLoader(object):
  def download(self,url):
    print 'begin download ', url

    if url is None:
      return None

    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/74.0.3729.169 Safari/537.36'
    headers = {'User-Agent':user_agent}
    sessions = requests.session()
    sessions.headers = headers
    r = sessions.get(url)

    if r.status_code == 200:
      r.encoding = 'utf-8'
      return r.text
    return None