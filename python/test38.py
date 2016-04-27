#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def myadd(x,y):
	return x + y
def hello(msg):
	if(msg == ''):
		print 'system exit'
		return True,0
	print '=====',msg
print myadd(1,2)
print myadd('zheng','fenglin')
print hello(msg='zhengfenglin')
