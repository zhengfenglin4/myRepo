#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class MyLimeter(object):
	__slots__ ='mynmame','myage','myhoppy'
	myname ='郑锋林'
	myage=28
	myhoppy='哈哈...'
if __name__ == '__main__':
	x=MyLimeter()
	print x.myname,x.myage,x.myhoppy
