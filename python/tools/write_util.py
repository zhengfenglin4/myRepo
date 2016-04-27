#!/usr/bin/env python
#coding=utf-8
from telnet_util import MyTelnet
import ftplib 
import shutil
import os
import time
class MyWrite():
	def __init__(self,fileName,filePath,info):
                self.__fileName = fileName
		self.__filePath = filePath
		self.__info = info
		self.copy()
		self.__write()
	def __write(self):
		self.__file = open(self.__filePath + '/' + self.__fileName,'w')
		self.__file.write(self.__info + '\n')
	def close(self):
		self.__file.close()
	def copy(self):
		times = time.strftime('%Y%m%d%H%M%S')
		file = self.__filePath + '/' + self.__fileName
		if self.is_exist_file(file):
			shutil.copy(file,file + times)
	def is_exist_file(self,file):
		if os.path.isfile(file): #file is exist
			return True
		else:
			return False #file is not exist
if __name__ == '__main__':
	mywrite = MyWrite('a','/tmp','hello')
	mywrite.close()
	print time.strftime('%Y%m%d%H%M%S')
