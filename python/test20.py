#!/usr/bin/env python
#coding:utf-8
#import winreg
import threading
import sys
sys.stderr = open('/dev/null')       # Silence silly warnings from paramiko
import paramiko as pm
sys.stderr = sys.__stderr__
import os
class AllowAllKeys(pm.MissingHostKeyPolicy):
   def missing_host_key(self, client, hostname, key):
       return

USER = 'wls81'
import time
#删除日志文件
#try:
#    os.remove('logfile.txt')
#except  WindowsError:
#    pass

def deletefile(file):
      #文件是否存在
    if os.path.exists(file):
        os.remove(file)
    else:
        pass 
deletefile("*.log")


def ssh2 (ip,username,passwd,war,port):
        #os.mkdir(r'log')
        client = pm.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(AllowAllKeys())
        client.connect(ip, username=username, password=passwd)

        channel = client.invoke_shell()
        stdin = channel.makefile('wb')
        stdout = channel.makefile('rb')
        telnet = '(sleep 1;) | telnet %s %s'%(ip,port)
        exit = 'exit'
        stdin.write("%s\n%s\n" %(telnet,exit))
        #文件写入
        file_object = open(ip+war+'.txt', 'a')
        file_object.write(stdout.read())
        file_object.close( )
        #print stdout.read()
        stdout.close()
        #stdin.close()
        client.close()
        file.close()
if __name__=='__main__':
    print time.strftime('%Y-%m-%d %H:%M:%S')
    username = "root"  #用户名
    threads = []   #多线程
    print "Begin......"
    file = open('ip_list.txt')
    for ip_lists in file.xreadlines():
                ip_list = ip_lists.split()
                HOST = ip_list[1]
		WAR  = ip_list[2]
                PASSWORD = ip_list[3]
                PORT = ip_list[4]
                a=threading.Thread(target=ssh2,args=(HOST,username,PASSWORD,WAR,PORT))
                a.start()
    file.close()
    print time.strftime('%Y-%m-%d %H:%M:%S')

