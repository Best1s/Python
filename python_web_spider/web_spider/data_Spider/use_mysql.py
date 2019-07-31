#coding: utf-8
'''
alter table table_name add  列名 数据类型  [after 插入位置]
alter table table_name change 列命 新列命 新数据类型
alter table table_name 列名称
alter table table_name rename 新表名
'''

#增加新用户 命令格式: grant 权限1， 权限2， ...权限n on 数据库名称.表名称 
# to 用户名@用户地址 identified by'密码'；

# greant select,insert,update,delete,create,drop on company.employee to username@x.x.x.x identified by '123';

#python 操作mysql 需要安装 mysqldb   pip install mysql-python
import MySQLdb
con = MySQLdb.connect(host='localhost',user='root',passwd='123456',port=3306,charset='utf-8')

'''
#cursor() 创建一个游标对象
#commit() 事务提交
#rollback() 事务回滚
#close() 关闭数据库连接
'''
cur = con.cursor()

# 游标对象使用  首先cursor()创建游标对象
# cur = con.cursor()
# execute()用来执行sql语句
# executemany()执行多条sql语句
# close() 关闭游标连接
# fetchone() 用来从结果中取一条记录，并将游标指向下一条记录。
# fetchmany() 从结果中取多条记录。
# fetchall() 从结果中取出所有记录
# scroll() 游标滚动

cur.execute(CREATE TABLE person (id int primary key,name varchar(20),age int)')
cur.execute('INSERT INTO PERSON VALUES (%d,%s,%d)',(1,'qiye1',20))

con.commit()
#查询 修改删除 和sqlite3 一样