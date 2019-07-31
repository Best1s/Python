#!/usr/bin/env python3

from socket import *
from time import ctime 
import os
HOST = ''
PORT = 22222
BUFSIZ = 1024
ADDR = (HOST,PORT)
print()
tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
  print('Waiting for connection...')
  tcpCliSock,addr = tcpSerSock.accept()
  print('...connected from:',addr)
  while True:
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
      break
    #else:
    #  print(data)
    if data == b'ls':
      data = os.listdir()
      for i in data:
        space = " "
        tcpCliSock.send(i.encode())
        
      break
    if data == b'os':
      data = os.name
      tcpCliSock.send(data.encode())
      break
    time = (ctime() + ' ').encode()
    tcpCliSock.send(time)
    tcpCliSock.send(data)
    #udpSerSock.sendto('[%s] %s' % (ctime(),data),addr)
    #de_data = data.decode('utf-8')
    #print(de_data)
    #data = '我收到了你的消息：' + de_data
    
  tcpCliSock.close()
tcpSerSock.close()