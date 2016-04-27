#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import urllib
if __name__ == '__main__':
	fabs = urllib.urlopen('hello.txt')
	print '获取文件中的所有信息:',fabs.info
	for line in fabs.readlines():
		print line
	fabs.close()
