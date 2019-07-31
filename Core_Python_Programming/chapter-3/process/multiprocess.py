import os
from multiprocessing import Process
from time import sleep
#def child code
def run_pro(name):
  print("Child process",name,os.getpid(),"Running...")
if __name__ == '__main__':
  print('Parent process ',os.getpid())
  for i in range(5):
    p = Process(target=run_pro,args=(str(i),))
    print("Process will start.")
    p.start()
  #print("test")
  p.join()
  print("Process end.")