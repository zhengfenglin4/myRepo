#!/usr/bin/env python
#coding=utf-8
import re
import os
import time
def is_exist_file(file):
	if os.path.isfile(file): #file is exist
		return True
	else:
		return False #file is not exist
def read_config(file='test.properties'):
	data = []
	digit = re.compile(r'(\d{5,})')
	try:
		lines = open(file,'r')
	except IOError:
		print '打开%s文件失败,请确认%s是否存在' %(file,file)
	if is_exist_file(file):
		for line in lines:
			#print line
			isDigit = re.findall(digit,line)
			if isDigit:
				data.append(int(isDigit[0]))
				#data.insert(0,int(isDigit[0]))
    		data = list(set(data)) #去重
    		write_file(add_dev(data))
	else:
		error = open('error.txt','wb')
		error.write('filter file\n-------------------------------\n\n' + '%s文件不存在,无法排序' %file + '\n\n-------------------------------' )
		error.close()
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
	file.write(time.strftime('%Y-%m-%d %H:%M:%S') + '编译:\n')
        file.write('filter file\n-------------------------------\n\n' + s + '\n\n-------------------------------')
        print s
        file.close()
if __name__ == '__main__':
        read_config()
