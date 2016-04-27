#!/usr/bin/env python
#coding=utf-8
import re
#对列表去重
def uniq_list(list):
	newList = []
	for l in list:
		if l not in newList:
			newList.append(l)
	return newList
def read_config(file='test.properties'):
	data = []
        digit = re.compile(r'(\d{5,})')	
	lines = open(file,'r')
	for line in lines:
		#print line
                isDigit = re.findall(digit,line)
		if isDigit:
			data.append(int(isDigit[0]))
			#data.insert(0,int(isDigit[0]))
	data = list(set(data)) #去重

	#print '==============='
	#data = uniq_list(data)
	#print data
	
	#print_dev(add_dev(data))
	write_file(add_dev(data))
def add_dev(list,prefix = 'DEV'):
	newList = []
	for l in list:
		newList.append(prefix + str(l))
	return newList
def print_dev(list):
	s = ''
	for l in list:
		s = s + l + ','
	print s
def write_file(list):
	s = ''
	file = open('fiter.properties','w')
	for l in list:
			s = s + l + ','
        print s
	file.write(s[:-1])
	print s
	file.close()
if __name__ == '__main__':
	read_config()

