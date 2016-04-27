#!/usr/bin/env python
#coding=utf-8
import re
import os
def is_exist_file(file):
	if os.path.isfile(file): #file is exist
		return True
	else:
		return False #file is not exist
def read_config(file='test.properties'):
	data = []
	digit = re.compile(r'(\d{5,})')
	lines = open(file,'r')
	if is_exist_file(file):
		for line in lines:
			#print line
			isDigit = re.findall(digit,line)
			if isDigit:
				data.append(int(isDigit[0]))
				#data.insert(0,int(isDigit[0]))
    		data = list(set(data)) #去重
    		write_file(add_dev(data))
def add_dev(list,prefix = 'DEV'):
        newList = []
        for l in list:
                newList.append(prefix + str(l))
        return newList
def write_file(list):
        s = ''
		
        file = open('filter.properties','wb')
        for l in list:
						s = s + l + ','
        s = s[:-1]
        file.write('filter file\n-------------------------------\n\n' + s +'\n\n-------------------------------')
        print s
        file.close()
if __name__ == '__main__':
        read_config()
