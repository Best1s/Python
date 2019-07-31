#!/usr/bin/python
# -*- coding: utf-8 -*-
names = ["name1","name2","name3"]
for name in names:
  print(name)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
#motorcycles = []
motorcycles.append('test')
motorcycles.append('test')
motorcycles.append('test')
motorcycles.append('test2')
motorcycles.insert(1,"t1")
print(motorcycles)
del motorcycles[0]
print(motorcycles)
aa = motorcycles.pop(2)
print(aa)
count = 0
for i in motorcycles:
  count = count + 1
  if i == "test2":
      motorcycles.remove(i)
      print count
print(motorcycles)
dinners = ["xiaoming", "xiaohong", 'dabai', 'hello']
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
for i in dinners:
  print("dinner name is " + i)
nodinner = dinners.pop(2)
print(nodinner + "not eat dinner")
dinners.insert(0,"xiaobai")
print(dinners)
dinners.sort()
print (dinners)
dinners.sort(reverse=True)
dinners.reverse()
print (dinners)
print(len(dinners))