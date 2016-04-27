#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def fruitFun(fruitList):
	checked =['香蕉','橘子','香梨']
	for e in fruitList:
		if e not in checked:
			checked.append(e)
	print '--------欢迎使用水果信息管理系统------------'
	print '现有水果:'
	checked.sort()
	for item in checked:
		print item
	return checked
if __name__ == '__main__':
	fruits = ['苹果','香蕉','橘子','香梨','橙子','苹果','香蕉','西瓜']
	addFruit = raw_input('请输入你要添加的水果:')
	fruits.append(addFruit)
	fruitFun(fruits)
