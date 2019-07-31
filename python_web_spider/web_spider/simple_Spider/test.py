#coding: utf-8
import requests
from bs4 import BeautifulSoup

html = '''
<dl class="lemmaWgt-lemmaTitle lemmaWgt-lemmaTitle-">
<dd class="lemmaWgt-lemmaTitle-title">
<h1>www</h1>
<h2>（万维网缩写）</h2>
<a href="javascript:;" class="edit-lemma cmn-btn-hover-blue cmn-btn-28 j-edit-link" style="display: inline-block;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
<a class="lock-lemma" nslog-type="10003105" target="_blank" href="javascript:;" title="锁定"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_lock-lemma"></em>锁定</a>
<a href="/planet/talk?lemmaId=109924" target="_blank" class="lemma-discussion cmn-btn-hover-blue cmn-btn-28 j-discussion-link" nslog-type="90000102"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_discussion-solid"></em>讨论<span class="num" style="display: inline;">1</span></a>
</dd>
</dl>
<div class="lemma-summary" label-module="lemmaSummary">
<div class="para" label-module="para">WWW是<a target="_blank" href="/item/%E7%8E%AF%E7%90%83%E4%BF%A1%E6%81%AF%E7%BD%91/9377238" data-lemmaid="9377238">环球信息网</a>的缩写，（亦作“Web”、“WWW”、“'W3'”，<a target="_blank" href="/item/%E8%8B%B1%E6%96%87">英文</a>全称为“World Wide Web”），中文名字为“<a target="_blank" href="/item/%E4%B8%87%E7%BB%B4%E7%BD%91/215515" data-lemmaid="215515">万维网</a>”，"环球网"等，常简称为Web。 分为Web<a target="_blank" href="/item/%E5%AE%A2%E6%88%B7%E7%AB%AF/101081" data-lemmaid="101081">客户端</a>和Web服务器程序。 WWW可以让Web<a target="_blank" href="/item/%E5%AE%A2%E6%88%B7%E7%AB%AF/101081" data-lemmaid="101081">客户端</a>（常用<a target="_blank" href="/item/%E6%B5%8F%E8%A7%88%E5%99%A8/213911" data-lemmaid="213911">浏览器</a>）访问浏览Web<a target="_blank" href="/item/%E6%9C%8D%E5%8A%A1%E5%99%A8">服务器</a>上的页面。 是一个由许多互相链接的<a target="_blank" href="/item/%E8%B6%85%E6%96%87%E6%9C%AC/2832422" data-lemmaid="2832422">超文本</a>组成的系统，通过<a target="_blank" href="/item/%E4%BA%92%E8%81%94%E7%BD%91">互联网</a>访问。在这个系统中，每个有用的事物，称为一样“资源”；并且由一个全局“<a target="_blank" href="/item/%E7%BB%9F%E4%B8%80%E8%B5%84%E6%BA%90%E6%A0%87%E8%AF%86%E7%AC%A6/2890807" data-lemmaid="2890807">统一资源标识符</a>”（<a target="_blank" href="/item/URI">URI</a>）标识；这些资源通过<a target="_blank" href="/item/%E8%B6%85%E6%96%87%E6%9C%AC%E4%BC%A0%E8%BE%93%E5%8D%8F%E8%AE%AE/8535513" data-lemmaid="8535513">超文本传输协议</a>（Hypertext Transfer Protocol）传送给用户，而后者通过点击链接来获得资源。</div><div class="para" label-module="para"><a target="_blank" href="/item/%E4%B8%87%E7%BB%B4%E7%BD%91%E8%81%94%E7%9B%9F/1458269" data-lemmaid="1458269">万维网联盟</a>（<a target="_blank" href="/item/%E8%8B%B1%E8%AF%AD/109997" data-lemmaid="109997">英语</a>：World Wide Web Consortium，简称W3C），又称W3C理事会。1994年10月在<a target="_blank" href="/item/%E9%BA%BB%E7%9C%81%E7%90%86%E5%B7%A5%E5%AD%A6%E9%99%A2">麻省理工学院</a>（MIT）计算机科学实验室成立。万维网联盟的创建者是万维网的发明者蒂姆·伯纳斯-李。</div><div class="para" label-module="para">万维网并不等同<a target="_blank" href="/item/%E4%BA%92%E8%81%94%E7%BD%91/199186" data-lemmaid="199186">互联网</a>，万维网只是互联网所能提供的服务其中之一，是靠着互联网运行的一项服务。</div>
</div>
'''

def _get_new_data(soup):
  page_url = 'www.baidu.com'
  data = {}
  data['url'] = page_url
  title = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
  data['title'] = title.get_text()
  summary = soup.find('div',class_='lemma-summary')
  data['summary'] = summary.get_text()
  return data

a = 'www.baidu.com'
soup = BeautifulSoup(html,'html.parser')
#print soup.prettify()
b = _get_new_data(soup)
#title = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')

#summary = soup.find('div',class_='lemma-summary')

for i,val in b.items():
  print i.encode('utf-8'),val.encode('utf-8')











'''
url = 'https://baike.baidu.com/item/5g'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/74.0.3729.169 Safari/537.36'
    #user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
headers = {'User-Agent':user_agent}

sessions = requests.session()
sessions.headers = headers
r = sessions.get(url) #通过sessions 去get 访问  解决 TooManyRedirects 错误
#r = requests.get(url,headers,allow_redirects=False)
r.encoding = 'utf-8'
print r.status_code

print 
print '----------------'
print r.text
'''