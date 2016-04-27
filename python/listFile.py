#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import os
def ListDir(path,fun,par):
	print '-------start---------'
	for filesPath in par:
		print os.path.join(fun,filesPath)
	print '----------end------------'
if __name__ =="__main__":
	path = "/root"
	os.walk(path,ListDir,())
