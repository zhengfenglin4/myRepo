#!/usr/bin/env python
#-*- coding: utf-8 -*-  
import paramiko  
import threading  
def ssh2(ip,username,passwd,cmd):  
    try:  
        ssh = paramiko.SSHClient()  
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
        ssh.connect(ip,22,username,passwd,timeout=5)  
        for m in cmd:  
            stdin, stdout, stderr = ssh.exec_command(m)  
#           stdin.write("Y")   #简单交互，输入 ‘Y’   
            out = stdout.readlines()  
            #屏幕输出  
            for o in out:  
                print o,  
        print '%s\tOK\n'%(ip)  
        ssh.close()  
    except :  
        print '%s\tError\n'%(ip)  
if __name__=='__main__':  
    cmd = ['cal','echo hello!']#你要执行的命令列表  
    username = "test"  #用户名  
    passwd = "abcd1234"    #密码  
    threads = []   #多线程  
    print "Begin......" 
    file = open('ip_info.txt')
    for ip_lists in file.xreadlines():
		ip_list = ip_lists.split()
		ip = ip_list[1]
		passwd = ip_list[3]
    		a=threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))   
    		a.start()
    file.close() 
