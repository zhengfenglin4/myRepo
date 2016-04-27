#!/usr/bin/env python
#coding=utf-8
import telnetlib
import time
import sys
import os

def do_telnet(Host, Port, username, password, finish= '>'):
    #finish = '>'
    commands=['cd ', 'ls']
    #连接Telnet服务器
    tn = telnetlib.Telnet(Host, Port, timeout=1)
    tn.set_debuglevel(3)
    print '=====1==========' 
    #输入登录用户名
    tn.read_until("login: ")
    tn.write(str(username)+'\r\n')
    print '=====2==========='    
    # 输入登录密码
    tn.read_until("Password: ")
    #tn.set_debuglevel(2)
    tn.write(str(password)+'\r\n')
    #tn.set_debuglevel(3)
    #tn.read_until("finish")
    #tn.write('sh /home/test/hello.sh \n') 
    tn.write('md5sum perl-5.20.1.tar.gz \n')
    #执行多个命令方式
    #for command in commands:
    #    tn.write(command + '\n')
    
    tn.write("exit\n")
    print tn.read_all()
   
    print 'Finish!'

    tn.close()
    
if __name__=='__main__':
    #Host = raw_input("IP:")           # Telnet服务器IP
    Host = '192.168.59.129'
    #Port = raw_input("Port:")        # Telnet服务器端口
    username = 'test'          # 登录用户名
    finish = 'md5sum perl-5.20.1.tar.gz'       # 密码错误提示  
    do_telnet(Host, 23, username, 'abcd1234', finish)

