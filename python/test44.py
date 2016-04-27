#!/bin/usr/env python
#coding:utf-8
import socket
import sys
HOST = '192.168.131.128'
PORT = 10000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = (HOST,PORT)
print >>sys.stderr,'connection to %s port %s'%server_address
s.connect(server_address)
try:
    message = 'This is the message.It will be repeated'
    print >>sys.stderr,'sending %s'%message
    s.sendall(message)
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = s.recv(16)
        amount_received += len(data)
        print >>sys.stderr,'received %s' %data
finally:
    print >>sys.stderr,'closing socket'
    s.close()
