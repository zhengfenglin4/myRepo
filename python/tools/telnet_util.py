#!/usr/bin/env python
#coding=utf-8
import telnetlib
import time
import sys
import os
class MyTelnet():
	def __init__(self,Host,Port,UserName,Password):
		self.__Host = Host
		self.__Port = Port
		self.__UserName = UserName
		self.__Password = Password
		self.__connect()
	def __connect(self):
		try:
			self.__tel = telnetlib.Telnet(self.__Host)
			#self.__tel.set_debuglevel(3)
                	self.__tel.read_until('login:')
                	self.__tel.write(self.__UserName + '\r\n')
                	self.__tel.read_until('Password:')
                	self.__tel.write(self.__Password + '\r\n')
		except Exception,e:
                        raise e
	def do_action(self,cmds):

		#判断字符串
		if isinstance(cmds,str):
    			self.__tel.write(cmds + '\n')
		if isinstance(cmds,list):
			#执行多个命令方式
                	for cmd in cmds:
                        	self.__tel.write(cmd + '\n')
    		self.__tel.write("exit\n")
    		print self.__tel.read_all()
    		print 'Finish!'
		self.__tel.close()
if __name__=='__main__':
	cmd = 'md5sum perl-5.20.1.tar.gz'
	cmds = ['md5sum perl-5.20.1.tar.gz','ls -rt','df']
	mytel = MyTelnet('192.168.59.129',23,'test','abcd1234')
	mytel.do_action(cmd)
