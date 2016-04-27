#!/usr/bin/env python
#_*_ coding:utf-8 _*_
i = 1
while i<=5:
	name = raw_input('输入你的用户名:')
	age  = raw_input('输入你的年龄:')
	i = i + 1
	if name == 'zfl':
		continue
	print 'hello','你输入的名字是',name,'你输入的年龄是',age
