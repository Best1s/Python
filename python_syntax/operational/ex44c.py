# --*-- coding: utf-8 --*--
#定义Parent类 和三种方法
class Parent(object):
  def override(self):
    print "PARENT override()"
  def implicit(self):
    print "PARENT implicit()"
  def altered(self):
    print "PARENT altered()"
#继承Parent类,
class Child(Parent):
  #重写Parent中override方法
  def override(self):
    print "CHILD override()"
  #重写Parent中altered方法
  def altered(self):
    print "CHILD, BEFORE PARENT altered()"
    #继承Parent的altered方法并返回
    super(Child, self).altered()
    print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()