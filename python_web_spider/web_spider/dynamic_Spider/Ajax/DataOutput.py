#coding: utf-8
import sqlite3
class DataOutput(object):
  def __init__(self):
    self.cx = sqlite3.connect('MTime.db')
    self.create_table('MTime')
    self.datas=[]

  def create_table(self,table_name):
    '''
    创建数据表
    :param table_name:表名
    :return:
    '''
    values = '''
    id integer primary key,
    MovieId integer,
    MovieTitle varchar(40) NOT NULL,
    RatingFinal REAL NOT NULL DEFAULT 0.0,
    ROtherFinal REAL NOT NULL DEFAULT 0.0,
    RPictureFinal REAL NOT NULL DEFAULT 0.0,
    RDirectorFinal REAL NOT NULL DEFAULT 0.0,
    RStoryFinal REAL NOT NULL DEFAULT 0.0,
    Usercount integer NOT NULL DEFAULT 0,
    AttitudeCount integer NOT NULL DEFAULT 0,
    TodayBoxOffice varchar(20) NOT NULL,
    TodayBoxOffice1 varchar(30) NOT NULL,
    Rank integer NOT NULL DEFAULT 0,
    ShowDays integer NOT NULL DEFAULT 0,
    isRelease integer NOT NULL
    '''
    self.cx.execute('CREATE TABLE IF NOT EXISTS %s (%s);' % (table_name,values))
  
  def store_data(self,data):
    '''
    数据存储
    ：param data:
    : return:
    '''
    if data is None:
      return
    self.datas.append(data)
    if len(self.datas) > 10:
      self.output_db('MTime')

  def output_db(self,table_name):
    '''
    将数据存储到sqlite
    :return
    '''
    for data in self.datas:
      #try:
      sql = '''INSERT INTO %s (MovieId,MovieTitle,\
      RatingFinal,ROtherFinal,RPictureFinal,\
      RDirectorFinal,RStoryFinal,Usercount,\
      AttitudeCount,TodayBoxOffice,TodayBoxOffice1,\
      Rank,ShowDays,isRelease) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
      ''' % table_name
      self.cx.execute(sql,data)
      self.datas.remove(data)
      #except Exception,e:
      #  print "数据没有插入",data
      #  print "error inf:",e
    self.cx.commit()
      
  def output_end(self):
    '''
    关闭数据库
    ：return：
    '''
    if len(self.datas) > 0:
      self.output_db('MTime')
    self.cx.close()