#!/usr/bin/python
from collections import OrderedDict
from random import randint
order = OrderedDict()
for i in range(1,10):
  a = 'a' + str(i)
  order[a] = i**2
  #print(order)
for k,v in order.items():
  print(k + ": " + str(v),end="\t")
print()
class Die():
  def __init__(self,sides=6):
    self.sides =sides
  def roll_die(self):
    x = randint(1,self.sides)
    print("The " + str(self.sides) + " number is " + str(x))
new_side = Die(10)
new_20side = Die(20)
for i in range(1,10):
  new_side.roll_die()
  print(end="\t")
  new_20side.roll_die()
  print(end="\t")
print(new_side.sides)
print(new_20side.sides)