#!/usr/bin/env python
#coding=utf-8
import telnetlib
import time
import sys
import os
sys.path.append(r'tools')
import read_config_line
def do_telnet(Host,Port,username, password,finish='$',timeout=60):
    finish = '$'
    timeout = 60
    commands=['cd ', 'ls']
    #连接Telnet服务器
    tn = telnetlib.Telnet(Host, Port, timeout=1)
    #tn.set_debuglevel(3)
    #print '=====1==========' 
    #输入登录用户名
    tn.read_until("login: ")
    tn.write(str(username)+'\r\n')
    #print '=====2==========='    
    # 输入登录密码
    tn.read_until("Password: ")
    tn.write(str(password)+'\r\n')
    tn.write('sh /home/test/hello.sh \n') 
    tn.write('sh /home/test/hello2.sh \n')
    tn.read_until(finish,timeout)
    tn.write("exit\n")
    print tn.read_all()
    print 'Finish!'
    tn.close()
    
if __name__=='__main__':
    allConfig = read_config_line.readConfig()
    read_config_line.printConfig(allConfig)
    allConfig = allConfig['test-user']
    Host = allConfig['Hostname'] 
    username = allConfig['Username']
    password = allConfig['Password']
    do_telnet(Host,23,username,password)
 
