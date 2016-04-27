#!/usr/bin/env python
#-*-coding:utf-8-*-  
class Filter:
	def __init__(self):
		self.blocked = []
	def filter(self,sequence):
		return [x for x in sequence if x not in self.blocked]
class SPAMFilter(Filter):#继承Filter父类
	def __init__(self):
		self.blocked =  ['SPAM'] 
f = Filter()
#f.init()
print f.filter([1,2,3])
s = SPAMFilter()
#s.init()
print s.filter(['SPAM','A','B','C','D','E','F','G','SPAM'])
