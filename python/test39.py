#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Father:
	def __init__(self):
		print '我的初始化Father类中的方法'
		print '供以后调用'
class Son(Father):
	def __init__(self):
		print '我的初始化Son类中的方法'
		Father.__init__(self)

s = Son()
