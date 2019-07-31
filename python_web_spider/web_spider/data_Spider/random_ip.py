import random
def random_ip():
  ip =  str(random.randint(0,255)) + '.' + str(random.randint(0,255)) + '.' \
      + str(random.randint(0,255)) + '.' + str(random.randint(0,255)) + '\n'
  return ip

def write_ip1(num):
  n =  1
  with open ('ip1','w+') as ip1:
    while True:
      ip1.write(random_ip())
      n += 1
      if n > num:
        break
    ip1.close()
def write_ip2(num):
  with open ('ip2','w+') as ip2:
    for i in range(num):
      ip2.write(random_ip())
    ip2.close()

if __name__ == '__main__':
  print random_ip()
  num = 100
  num = num / 2
  write_ip1(num)
  write_ip2(num)

  
         

  