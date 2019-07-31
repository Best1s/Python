#!/usr/bin/env python3
from random import randrange,choice
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime
tlds = ('com','edu','net','org','gov')
for i in range(randrange(5,11)):
  print()
  dtint = randrange(maxsize)
  dtstr = ctime(dtint)
  llen = randrange(4,8)
  login = ''.join(choice(lc) for j in range((allen)) 
  dlen = randrange(llen,13)
  dom = ''.join(choice(lc) for j in range(dlen))
  print '%s::%s@%s.%s::%d-%d-%d' % (dtint,login,dom,choice(tlds),dtint,llen,dlen))
print(dlen)