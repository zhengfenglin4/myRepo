#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import socket
import commands
host = '192.168.59.128'
port = 1234
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
while 1:
	cmd = raw_input("please input cmd:")
	s.sendall(cmd)
	data = s.recv(1024)
	print data
s.close()
