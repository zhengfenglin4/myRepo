#!/usr/bin/env python
#coding=utf-8
import re
import sys
import telnetlib
import ftplib
import os
finish = '>'
enter = '\n'
CONST_BUFFER_SIZE = 1000000
class MyTelnet(object):
	__finish = '>'
	def __init__(self,hostname,username,password):
		self.__hostname = hostname
		self.__username = username
		self.__password = password
		self.__createConnect()
	def __createConnect(self):
		try:
			self.__tn = telnetlib.Telnet(self.__hostname)
			self.__tn.read_until('login:')
			self.__tn.write(self.__username + '\n')
			self.__tn.read_until('Password:')
			self.__tn.write(self.__password + '\n')
			self.__tn.read_until(self.__finish)
		except Exception,e:
			self = None
			raise e
	def paraseCommand(self,command,finish='>',timeout=60):
		print 'do command "%s"' % command
		self.__tn.write(command+'\n')
		text=self.__tn.read_until(finish,timeout)
		return text
	def paraseCommands(self,commands,finish='>',timeout=60):
		for command in commands:
			print 'do command "%s"' % command
                	self.__tn.write(command+'\n')
                	text=self.__tn.read_until(finish,timeout)
	def close(self):
		self.__tn.write('exit\n')
class MyFtp():
	def __init__(self,hostname,username,password):
		self.__hostname = hostname
		self.__username = username
		self.__password = password
		self.__createConnect()
	def __createConnect(self):
		self.__ftp = ftplib.FTP(self.__hostname)
		self.__ftp.login(self.__username,self.__password)

	def ftp_down(self,remotedir,localdir,filename):
		try:
			if not os.path.exists(localdir):
				os.makedir(localdir)
			localfile = localdir + '/' + filename
			file = open(localfile,'wb').write
			print 'cd' + remotedir
			self.__ftp.cwd(remotedir)
			print 'download filename=%s/%s' %(remotedir,filename)
			self.__ftp.retrbinary("RETR %s" % filename,file,CONST_BUFFER_SIZE)
			return True
		except ftplib.error_perm:
			raise e
			return False
	def ftp_up(self,remotedir,localdir,filename):
                try:
                        localfile = localdir + '/' + filename
                        file = open(localfile,'rb')
                        print 'cd' + remotedir
                        self.__ftp.cwd(remotedir)
                       #print 'upload filename=%s'  %(filename))
                        self.__ftp.storbinary("STOR %s" % os.path.basename(filename),file,CONST_BUFFER_SIZE)
                        return True
                except ftplib.error_perm:
                        raise e
                        return False
	def close(self):
		self.__ftp.quit()
def main():
	host='192.168.59.128'
	username='test'
	password='abcd1234'
	#tn=MyTelnet(host,username,password)
	tn=MyFtp(host,username,password)
	#print text
if __name__ == '__main__':
	main()
