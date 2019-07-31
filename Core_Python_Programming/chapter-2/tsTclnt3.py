#!/usr/bin/env python3

from socket import *

#HOST = 'localhost'
#PORT = 22222
HOST = ''
PORT = 0
BUFSIZ =1024

HOST = input('Plase input host(default localhost):')
if not HOST:
  HOST = 'localhost'
PORT = input('Plase input port(default 22222):')
if not PORT:
  PORT = 22222
else:
  PORT = int(PORT)
ADDR = (HOST,PORT)
tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
  data = input('> ')
  print(data)
  if data == 'q':
    tcpCliSock.close()
    break
  tcpCliSock.send(data.encode())
  data = tcpCliSock.recv(BUFSIZ)
  if not data:
    break
  print(data.decode('utf-8'))
tcpCliSock.close()