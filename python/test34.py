#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def login(username,password):
	msg = ''
	if (username == 'admin') and (password == 'admin'):
		msg = '登录成功'
	else:
		msg = '登录失败'
	return msg
def validate(usernames):
	if (len(usernames) > 4 and len(usernames) < 12 ):
		return usernames
def operat(x,y):
	return x + y
def add1(a):
	return a + 1
def add2(a,b):
	return a + b
def add3(a,b,c):
	return a + b + c
print apply(login,('admin','admin'))
print filter(validate,('admin','abcdfsdafs','mas','bb','fdsafsaa','zfadsffsdafsafsafsaf'))
print reduce(operat,(1,23,222,6,5))
a1 = [1,2,3,4,5]
a2 = [1,2,3,4,5]
a3 = [1,2,3,4,5]
print map(add1,a1)
print map(add2,a1,a2)
print map(add3,a1,a2,a3)
