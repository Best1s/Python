#coding: utf-8
import cPickle  
import hashlib

class UrlManager(object):

  def __init__(self):
    self.new_urls = self.load_progress('new_urls.txt')
    self.old_urls = self.load_progress('old_urls.txt')

  def has_new_url(self):
    return self.new_url_size() != 0
    #return new_url_size() != 0

  def get_new_url(self):
    new_url = self.new_urls.pop()
    m = hashlib.md5()
    m.update(new_url)
    self.old_urls.add(m.hexdigest()[8:-8])
    return new_url

  def add_new_url(self,url):
    if url is None:
      return
    m = hashlib.md5()
    m.update(url)
    url_md5 = m.hexdigest()[8:-8]
    if url not in self.new_urls and url_md5 not in self.old_urls:
      self.new_urls.add(url)

  def add_new_urls(self,urls):
    if urls is None or len(urls) == 0:
      return
    for url in urls:
      self.add_new_url(url)

  def new_url_size(self):
    print 'url num is ', len(self.new_urls)
    return len(self.new_urls)

  def old_url_size(self):
    return len(self.old_urls)

  #cPickle将内存中的对象转换成为文本流  cPickle是用C编码的，在运行效率上比pickle要高
  #对象 -> 文本 -> 文件
  #pickle.dump(), pickle.load(), cPickle
  #dump()函数接受一个数据对象和一个文件句柄作为参数，把数据对象以特定的格式保存到给定的文件中。
  #当我们使用load() 函数从文件中取出已保存的对象时，pickle知道如何恢复这些对象到它们本来的格式
  #dumps()函数执行和dump()函数相同的序列化。
  #loads()函数执行和load()函数一样的反序列化。
  def save_progress(self,path,data):
    with open(path,'wb') as f:
      cPickle.dump(data,f)

  def load_progress(self,path):
    print '[+] from file loading: %s' %path
    try:
      with open(path,'rb') as f:
        tmp = cPickle.load(f)
        return tmp
    except:
      print '[!] not file, Create: %s' % path
    return set()
    