#coding:utf-8
import sqlite3
'''

#con = sqlite3.connect(':memory:') 内存中创建

#cursor() 创建一个游标对象
#commit() 事务提交
#rollback() 事务回滚
#close() 关闭数据库连接

# 游标对象使用  首先cursor()创建游标对象
# cur = con.cursor()
# execute()用来执行sql语句
# executemany()执行多条sql语句
# close() 关闭游标连接
# fetchone() 用来从结果中取一条记录，并将游标指向下一条记录。
# fetchmany() 从结果中取多条记录。
# fetchall() 从结果中取出所有记录
# scroll() 游标滚动
'''
con = sqlite3.connect("test.db")
cur = con.cursor()

#建表
try:
  cur.execute('CREATE TABLE person (id integer primary key,name varchar(20),age integer)')
except:
  pass
#插入数据
data = "0,'qiye',20"
cur.execute('INSERT INTO person VALUES ($s)' % data)  #不安全容易sql注入 ，另一种占位符号
cur.execute('INSERT INTO PERSON VALUES (?,?,?)',(1,'qiye1',20))

cur.executemany('INSERT INTO PERSON VALUES (?,?,?)',[(2,'qiye2',20),(3,'qiye3',20),(4,'qiye4',20)])
# 两种方法不会立即生效 需要con对象提交
con.commit()

#如果错误 可以回滚操作
#con.rollback()

#查询数据  fetchall() 获取所有数据 返回二维的列表  fetchone()返回元组
cur.execute('SELECT * FROM person')

res = cur.fetchall()
for line in res:
  print line
  cur.execute('SELECT * FROM person')
  res = cur.fetchone()
  print res

#修改和删除
cur.execute('UPDATE person SET name=? WHERE id=?',('rose',2))
cur.execute('DELETE FROM person WHERE id=?',(1,))

con.commit()
con.close()

#插入中文或者修改中文需要在字符串前加 u
