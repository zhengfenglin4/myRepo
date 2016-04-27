#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
Created on 2015年9月23日

@author: zhengfenglin
本地MD5SUM
'''
import hashlib
import time
import os
import re
class Md5sum():
    global point 
    point = '*'*50
    def __md5sum(self,filename):
        md5file = open(filename,'rb')
        fmd5 = hashlib.md5(md5file.read()).hexdigest()
        md5file.close()
        return fmd5 + '  %s' %filename
    '''
    def __init__(self,filenames):
        file = open('md5.log','a')
        file.write('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\tMD5 info\n' + point +'\n')
        filenames = filenames.split(',')
        for filename in filenames:
            info = self.__md5sum(filename)
            #print info
            file.write(info + '\n')
        file.write(point)
        file.close()
    '''
    def test(self,filenames):
	print filenames
	file_list = filenames.rstrip().split(',')
	print file_list
	for file in file_list:
		print file
if __name__ == '__main__':
    #print os.chdir('D:\\tmp\\N-IPFT_20150804_20_71')
    #print os.getcwd()
    #Md5sum('/root/CitrixReceiver.exe')
    Md5sum().test('/root/CitrixReceiver.exe,/root/python/md5sum-test.py')
