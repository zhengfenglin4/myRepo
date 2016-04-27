#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Person(object):
	def __init__(self,name):
		self.name=name
		print '我是一个人，初始化名字是：%s' %self.name
class Ordinary(Person):
	def __init__(self):
		super(Ordinary,self).__init__()
		print '我是一个普通人'

if __name__ == '__main__':
	print issubclass(Ordinary,Person)
	person=Person('dcy')
	print isinstance(person,Person)
