#!/usr/bin/env python
#-*-coding:utf-8-*- 
file = open('ip_info.txt')
try:
	for ip_lists in file.xreadlines():
		ip_list = ip_lists.split() 
		print 'stg=',ip_list[0],'ip=',ip_list[1],'war=',ip_list[2],'passwd=',ip_list[3]
finally:
	file.close( )
