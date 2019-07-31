import os 
from time import sleep
if __name__ == '__main__':
  print('current Process start ...',(os.getpid()))
  pid = os.fork()
  if pid < 0:
    print("error in fork")
  elif pid == 0:
    print("I am child process ",os.getpid(), " and my parent process is ",os.getppid())
  else:
    print("I ",os.getpid() , "created a chlid process ",pid)
sleep(2)
print("I am ",os.getpid())