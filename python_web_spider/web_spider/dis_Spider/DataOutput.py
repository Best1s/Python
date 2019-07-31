#coding:utf-8
import codecs
import time

#store_data(data) 方法用于将解析出来的数据存到内存中
#output_html()用于将存储数据输出为指定文件格式

class DataOutput(object):

  def __init__(self):
    self.filepath = 'baike_%s.html' % (time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime()))
    self.output_head(self.filepath)
    self.datas = []
    
  def store_data(self,data):
    if data is None:
      return
    self.datas.append(data)
    if len(self.datas) > 0:
      self.output_html(self.filepath)

  def output_head(self,path):
    fout = codecs.open(path,'w',encoding='utf-8')
    fout.write('<html>')
    fout.write('<body>')
    fout.write('<table>')
    fout.close

  def output_html(self,path):      #如果数据很多 需要采用分批存储办法  数据都暂时存在了内存中
    fout = codecs.open(path,'a',encoding='utf-8')
    for data in self.datas:
      fout.write("<tr>")
      fout.write("<td>%s</td>" % data ['url'])
      fout.write("<td>%s</td>" % data ['title'])
      fout.write("<td>%s</td>" % data ['summary'])
      fout.write("<tr>")
      self.datas.remove(data)

  def output_end(self,path):
    fout = codecs.open(path,'a',encoding='utf-8')
    fout.write("</table")
    fout.write('</body>')
    fout.write('</html>')
    fout.close()
