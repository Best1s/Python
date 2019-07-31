# -*- coding: utf-8 -*-
import web
import os

class Index(object):
  def GET(self):
    #return render.index()
    form = web.input(name = None, greet = None)
    #form2 = web.input(name = 'None')
    greeting = "%s %s" % (form.name, form.greet)
    if form.name == "admin" and form.greet == "admin":
      return render.admin()
    else:
      return render.index(greeting = greeting)
    #return render.hello_form()
  def POST(self):
    form = web.input(name = "Nobody",greet = "None")
    greeting = "%s %s" % (form.name, form.greet)
    return render.index(greeting = greeting)

class Login(object):
  def GET(self):
    return render.login(state=False)
  def POST(self):
    form = web.input(username = None,password = None)
    if form.username == "admin" and form.password == "admin":
      return render.admin()
    else:
      return render.login(state=True)
      
class Upload(object):
  def GET(self):
    return render.upload()
  def POST(self):
    x = web.input(myfile={})
    web.debug(x['myfile'].filename) # 这里是文件名
    web.debug(x['myfile'].value) # 这里是文件内容
    web.debug(x['myfile'].file.read()) # 或者使用一个文件对象
    raise web.seeother('/upload')

class foo:
  def GET(self):
    form = web.input(name = None)
    return render.foo(greeting = form.name)
class layout:
  def GET(self):
    return render.layout("test")

if __name__ == "__main__":
  urls = (
  '/','Index',
  '/admin', 'Login',
  '/upload','Upload'  
  )
  
  app = web.application(urls, globals())
  render = web.template.render('templates/', base = "layout")
  app.run()