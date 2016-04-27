#!/usr/bin/env python
#coding=utf-8
from telnet_util import MyTelnet
import ftplib 
import os
import socket
class MyFtp():
	BUFFER_SIZE=8192
	#初始化
	def __init__(self,hostname,username,password,localFilePath):
                self.__hostname = hostname
                self.__username = username
                self.__password = password
		self.__localFilePath = localFilePath
		self.chLoadPath()
                self.connect()
	#登录FTP
	def connect(self):
		try:
			self.__ftp = ftplib.FTP(self.__hostname)
			#打开调试日志级别
			self.__ftp.set_debuglevel(2)
			self.__ftp.login(self.__username,self.__password)
		except socket.error,socket.gaierror:
			print("FTP 不能登录")
			sys.exit(0)
	#退出
	def quit(self):
		self.__ftp.quit()
	def download(self,fileName,filePath=os.getcwd()):
		self.__ftp.cwd(filePath)
		filePath = filePath + '/' + fileName
		f = open(fileName,'wb').write
		try:
			self.__ftp.retrbinary("RETR %s"%filePath,f,self.BUFFER_SIZE)
		except ftplib.error_perm:
			print '确认是否是文件路径有问题,目前路径是%s' %fileName
			return False
		self.md5sum(fileName)
		self.quit()
		return True
	def upload(self,fileName,filePath=os.getcwd()):
		#切换远程目录
		self.__ftp.cwd(filePath)
		#远程目录
		remdir = filePath + '/' + fileName 
		#本地目录
                localName = self.__localFilePath + '/' + fileName
		#打开本地要上传的文件
                f = open(localName,'rb')
                try:
                       	self.__ftp.storbinary("STOR %s"%remdir,f,self.BUFFER_SIZE)
                except ftplib.error_perm:
                        print '确认是否是文件路径有问题,目前路径是%s' %remdir
                        return False
                self.md5sum(fileName)
                self.quit()
                return True
	def chLoadPath(self):
		os.chdir(self.__localFilePath)
		print '本地路径为:',self.__localFilePath
	def md5sum(self,fileName):
		print '--------下载到本机的md5sum %s信息------------' %fileName
		os.system('md5sum %s' %fileName)
if __name__ == '__main__':
	cmd = 'md5sum perl-5.20.1.tar.gz'
        mytel = MyTelnet('192.168.59.129',23,'test','abcd1234')
        mytel.do_action(cmd)
	
	myftp = MyFtp('192.168.59.129','test','abcd1234','/root/tools')
	#myftp.download('hello.tar','/home/test')
	myftp.upload('perl-5.20.1.tar.gz','/home/test')
