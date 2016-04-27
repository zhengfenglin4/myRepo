#!/usr/bin/env python
#coding=utf-8
import re
def readConfig(filename='info.properties'):
	#定义字典
	datas = {}
	data = None
	with open(filename) as config:
		lines = config.readlines()
	for line in lines:
		#替换
		line = re.sub(r'\s','',line)
		if line.startswith('#'): 
			continue
		if line == '': 
			continue
		if line.startswith('[') and line.endswith(']'):
			data = line[1:-1]
			datas[data] = {}
		else:
			item = line.split('=',1)
			key = item[0]
			value = item[1]
			if data:
				datas[data][key] = value
	return datas
def printConfig(datas):
	#字典遍例
	for(key,value) in datas.items():
		print '['+key+']'
		for(subkey,subvalue) in value.items():
			print subkey+'='+subvalue
if __name__ == '__main__':
	config = readConfig()
	printConfig(config)
