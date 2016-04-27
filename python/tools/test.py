##!/usr/bin/env python
#coding=utf-8
import os
os.chdir("/root/")
from ftplib import FTP            #加载ftp模块
ftp=FTP()                         #设置变量
ftp.set_debuglevel(2)             #打开调试级别2，显示详细信息
ftp.connect("192.168.59.129")          #连接的ftp sever和端口
ftp.login("root","abcd1234")      #连接的用户名，密码
print ftp.getwelcome()            #打印出欢迎信息
ftp.cwd("/home/test")                #进入远程目录
bufsize=1024                      #设置的缓冲区大小
filename="hello.tar"           #需要下载的文件
file_handle=open(filename,"wb").write #以写模式在本地打开文件
ftp.retrbinary("RETR %s" %filename,file_handle,bufsize) #接收服务器上文件并写入本地文件
ftp.set_debuglevel(0)             #关闭调试模式
ftp.quit()                        #退出ftp
