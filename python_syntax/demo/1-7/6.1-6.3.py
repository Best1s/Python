#!/usr/bin/python3
import random
info = {"fist_name":"zhang","last_name":"san","age":"18","city":"beijing"}
print(info)
function = {"append":"追加","insert":"插入","pop":"删除并赋值"}
print(function["append"])
for k,v in info.items():
  print(k +" "+ v)
for func in function.keys():
  print(func)
for func in sorted(set(function.values())):
  print(func)
alien = []
for i in range(1,10):
  mode = random.randint(1,3)
  speed = 0
  color = ""
  points = 0
  if mode == 1:
    speed = "slow"
    color = "green"
    points = 5
  elif mode == 2:
    speed = "medium"
    color = "yellow"
    points = 10
  elif mode == 3:
    speed = "fast"
    color = "red"
    points = 15
  new_alien = {"color":color,"points":points,"speed":speed}
  alien.append(new_alien)
for i in alien:
  print(i)
  

