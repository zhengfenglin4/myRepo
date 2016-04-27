#!/usr/bin/env python
#-*-coding:utf-8-*-  
class  Person:
	def setName(self,name):
		self.name = name
	def getName(self):
		return self.name
	def setAge(self,age):
		self.age = age
	def getAge(self):
		return self.age
	def greet(self):
		print "hello ,world! I'm %s,%s" % (self.name, self.age)
foo = Person()
bar = Person()
foo.setName('Luke')
foo.setAge(20)
bar.setName('Anakin')
bar.setAge(29)
foo.greet()
bar.greet()
