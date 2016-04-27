#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import socket
import commands
s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
hostName = socket.gethostname()
print 'HOSTName:',hostName
port = 2345
s.bind((hostName,port))
s.listen(5)
while True:
	conn,addr = s.accept()
	print '连接来自:',addr
	conn.send('恭喜你！一个简单的服务器创建成功！')
	while 1:
                data = conn.recv(1024)
                cmd_status,cmd_result = commands.getstatusoutput(data)
                if len(cmd_result.strip()) == 0:
                        conn.sendall('Done.')
                else:
                        conn.sendall(cmd_result)
	conn.close()
s.close()
