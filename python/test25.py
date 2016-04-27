#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#定义自己的class类

class MyClass():
	__username = '' #私有属性
	def __init__(self,username):
		self.__username = username
	def getUserName(self):
		return self.__username
if __name__ == '__main__':
	myClass = MyClass('zhengfenglin')
	print myClass.getUserName()
