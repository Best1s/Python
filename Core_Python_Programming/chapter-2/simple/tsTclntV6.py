#!/usr/bin/env python3

from socket import *

HOST = '::1'
PORT = 22222
BUFSIZ =1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET6,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
  data = input('> ').encode()
  if not data:
    break
  tcpCliSock.send(data)
  data = tcpCliSock.recv(BUFSIZ)
  if not data:
    break
  print(data.decode('utf-8'))
tcpCliSock.close()