#!/usr/bin/env python
# _*_ coding:utf-8 _*_

def abstract():
	raise NotImplementedError('对不起，不允许实例化超类')
class MyClothStore:
	def __init__(self):
		self.fname='SIMILE'
		print self.fname
		if self.__class__ is MyClothStore:
			abstract()
class MyGrilCloth(MyClothStore):
	def __init__(self):
		self.clothname='甜美可私服'
		print self.fname
class MyBoyCloth(MyClothStore):
	def __init(self):
		self.clothname='太可思西服'
		print self.clothname
class BoyCloth(MyClothStore,MyBoyCloth):
	def __init__(self,AdultName,AdultMake,AdultPrice,AdultWash):
		print '这件男装在全国的总店名称是:'
		MyClothStore.__init__(self)
		print '这件男装的名称是:'
		MyBoyCloth.__init__(self)
		self.AdultName=AdultName
		print '这件衣服的名称是:%s'%self.AdultName
		self.AdultMake=AdultMake
		print '这件衣服的制造是:%s'%self.AdultMake
		self.AdultPrice=AdultPrice
		print '这件衣服的价格是:%s'%self.AdultPrice
		self.AdultWash=AdultWash
		print '这件衣服只能被是:%s'%self.AdultWash

class AdultCloth(MyClothStore,MyGrilCloth):
        def __init__(self,AdultName,AdultMake,AdultPrice,AdultWash):
                print '这件男装在全国的总店名称是:'
                MyClothStore.__init__(self)
                print '这件男装的名称是:'
                MyGrilCloth.__init__(self)
                self.AdultName=AdultName
                print '这件衣服的名称是:%s'%self.AdultName
                self.AdultMake=AdultMake
                print '这件衣服的制造是:%s'%self.AdultMake
                self.AdultPrice=AdultPrice
                print '这件衣服的价格是:%s'%self.AdultPrice
                self.AdultWash=AdultWash
                print '这件衣服只能被是:%s'%self.AdultWash

if __name__ == '__main__':
	adultcloth=AdultCloth('dcy','guochan','1500RBM','干洗')
	adultcloth=BoyCloth('郑锋林','guochan','2500RBM','干洗')
