#simple  web spider
import urllib
from bs4 import BeautifulSoup
#import urllib.request
#request = urllib2.urlopen('http://www.zhihu.com')
with open ("index.xml","r") as read_xml:
  read_xml = read_xml.read()
#html = request.read()
read_xml = BeautifulSoup(read_xml,from_encoding="utf-8")
#print(read_xml)
read_xml.title.name = "data"
print(read_xml.data)
