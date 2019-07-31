#coding:utf-8
import re
import urlparse
from bs4 import BeautifulSoup

class HtmlParser(object):

  def parser(self,page_url,html_cont):
    '''
    用于解析网页内容，抽取URL和数据
    ：param page_url: 下载页面URL
    : param html_cont: 下载的页面内容
    ：return: 返回url 和数据
    '''
    if page_url is None or html_cont is None:
      print 'Error page_url or html_cont is None'
      return
    print 'download seccussful,begin parser!'
    soup = BeautifulSoup(html_cont,'html.parser') #,from_encoding='utf-8'默认就是 utf-8 不用加

    new_urls = self._get_new_urls(page_url,soup)

    new_data = self._get_new_data(page_url,soup)
    #print '-'*(90)
    #for i,val in new_data.items():
    #  print i,val

    return new_urls,new_data

  def _get_new_urls(self,page_url,soup):
    '''
    抽取新的url集合
    ：param page_url: 下载 页面的url
    : param soup:soup
    : return: 返回新的url集合
    '''
    new_urls = set()
    #抽取符合要求的a标记
    #/item/%E4%B8%87%E7%BB%B4%E7%BD%91/215515
    #soup.find_all("a", {"target": "_blank", "href": re.compile("/item/(%.{2})+$")})
    #links = soup.find_all('a',href=re.compile(r'/item/*'))
    links = soup.find_all('a',{"target": "_blank", "href": re.compile("/item/(%.{2})+$")})
    for link in links:
      #提取href属性
      new_url = link['href']
      #print new_url
      #拼接成完整网址
      new_full_url = urlparse.urljoin(page_url,new_url)   #urlparse.urljoin 将当前网址 和相对网址拼接
      #print new_full_url
      new_urls.add(new_full_url)
    return new_urls

  def _get_new_data(self,page_url,soup):
    '''
    抽取所有数据
    ：param page_url:下载页面的url
    ：param soup:
    : return:返回有效数据
    '''
    data = {}
    data['url'] = page_url
    title = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
    data['title'] = title.get_text()
    summary = soup.find('div',class_='lemma-summary')
    data['summary'] = summary.get_text()
    return data