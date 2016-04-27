#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import sys
def hello(str='None'):
	print str,'hello world!'

if __name__ == '__main__':
	str = sys.argv[1]
	hello(str)

