#coding:utf-8
'''
str1 = 'There is a tree behind the house.'[:-1].split()
str2 = 'A big tree is cut down there.'[:-1].split()
n = 0
togeter = []
for i in str1:
  if i in str2:
     togeter.append(i)
for max_word in togeter:
  if len(max_word) < n:
    n = len(max_word)
    max_word= n
print max_word
'''
'''
def fun():
  for i in range(20):
      x = yield i
      print('good',x)
for x in fun():
    print(x)
'''

'''
def fab(max): 
   n, a, b = 0, 0, 1 
   while n < max: 
       print b 
       a, b = b, a + b 
       n = n + 1
fab(5)
#复用性查 return 返回为None
'''

'''
def fab(max): 
   n, a, b = 0, 0, 1 
   L = [] 
   while n < max: 
       L.append(b) 
       a, b = b, a + b 
       n = n + 1 
   return L
for n in fab(5): 
  print n
#该函数在运行中占用的内存会随着参数 max 的增大而增大，如果要控制内存占用，最好不要用 List
'''


'''通过 iterable 对象来迭代
1
for i in range(1000): pass
会导致生成一个 1000 个元素的 List，而代码：

1
for i in xrange(1000): pass
则不会生成一个 1000 个元素的 List，而是在每次迭代中返回下一个数值，
内存空间占用很小。因为 xrange 不返回 List，而是返回一个 iterable 对象。
利用 iterable 我们可以把 fab 函数改写为一个支持 iterable 的 class'''

'''
class Fab(object): 
 
   def __init__(self, max): 
       self.max = max 
       self.n, self.a, self.b = 0, 0, 1 
 
   def __iter__(self): 
       return self 
 
   def next(self): 
       if self.n < self.max: 
           r = self.b 
           self.a, self.b = self.b, self.a + self.b 
           self.n = self.n + 1 
           return r 
       raise StopIteration()
for n in Fab(5):   #Fab 类通过 next() 不断返回数列的下一个数，内存占用始终为常数
  print n
'''


'''
使用 class 改写的这个版本，代码远远没有第一版的 fab 函数来得简洁。
如果我们想要保持第一版 fab 函数的简洁性，同时又要获得 iterable 的效果，yield 就派上用场了：'''
#第四个版本的 fab 和第一版相比，仅仅把 print b 改为了 yield b，就在保持简洁性的同时获得了 iterable 的效果

def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b 
        # print b 
        a, b = b, a + b 
        n = n + 1
for n in fab(5): 
  print n
