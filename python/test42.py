#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def arrayList(obj,index):
	try:
		return obj[index]
	except (IndexError),e:
		print e 
if __name__ == '__main__':
	userList = ['001','002','003','004','005','006','007']
	print arrayList(userList,7)
	print '=======1======'
