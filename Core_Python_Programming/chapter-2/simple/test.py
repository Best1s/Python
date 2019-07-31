from time import ctime 
a = 'bbbbb'
print('[%s]' % ctime())
en_ctime = ctime().encode('utf-8')
print('编码后输出：',en_ctime)
print(type(en_ctime))
print('解码后输出',en_ctime.decode())
#de_ctime = ctime().decode('utf-8')
print('[%s] \t%s' % (ctime().encode,a))
print(ctime().encode())

print('this is a test '.encode())
  