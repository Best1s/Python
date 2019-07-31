#coding:utf-8
#pymongo库操作MongoDB需要提前安装 
import pymongo

#建立连接  主要需要host,port 连接的三种方式
client = pymongo.MongoClient() #使用默认
#client = pymongo.MongoClient('localhost',27017) #指定IP 和端口
#client = pymongo.MongoClient('mongodb://localhost',27017) #指定url 和端口

db = client.python     #一个MongoDB可以支持多个独立的数据库，使用MongoCLient的属性方法访问数据库

# 如果是数据库名字导致属性不可用可以通过字典访问数据库
db = clinet['python']

#获取一个集合
collection = db.books   #或者   collection = db['books']

#插入  MongoDB是以JSON类的形式保存 如果没有_id键值，系统会自动添加 唯一
book = {"author":"zhang",
  "text":"My first book!",
  "tags":["爬虫","python","网络"],
  "data":datetime.datetime.utcnow()
  }
book_id = collection.insert(book)

#迭送 批量插入

book = {"author":"wang",
  "text":"My second book!",
  "tags":["爬虫","python","网络"],
  "data":datetime.datetime.utcnow()
  },{"author":"li",
  "text":"My third book!",
  "tags":["hack","socket","网络"],
  "data":datetime.datetime.utcnow()
  }
book_id = collection.insert(books)

#查询 find_one   返回一个符合查询的文件，无匹配返回None  : collection.find_one()

collection.find_one({'author':'zhang'})

#通过ID 也可以查询

collection.find_one({'_id':ObjectId('5d149b2a33613c0d2b69a325')})

#如果想获取多个文档 使用 find() 方法
for book in collection.find():
  print book

#可以传入条件限制查询结果：

for book in collection.find({"author":"wang"}):
  print book

#查询符合条件的文件有多少  count() 方法    
collection.find({"author":"wang"}).count()

#修改文档 update()和save()      save() 方法通过传入的文档来替换已有文档。
collection.update({"author":"li"},{"$set":{"text":"li first book"}})
