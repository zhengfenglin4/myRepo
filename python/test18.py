#!/usr/bin/env python
#coding=utf-8
from sys import argv
print  "argv=",len(argv)
script='NULL';first='NULL';second='NULL';third='NULL'
try:
	script,first,second,third = argv
except ValueError:
	print "列表长度过长"
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
