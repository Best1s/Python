#!/usr/bin/env python

from socket import *

HOST = 'localhost'
PORT = 22222
BUFSIZ =1024
ADDR = (HOST,PORT)

tcpCliSock = sockect(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
  data = raw_input('> ')
  if not data:
    break
  tcpCliSock.send(data)
  data = tcpCliSock.recv(BUFSIZ)
  if not data:
    break
  print data
tcpCliSock.close()