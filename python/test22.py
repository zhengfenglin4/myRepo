#!/usr/bin/env python
# -*- coding: utf-8 -*-  
import telnetlib
'''Telnet远程登录：Windows客户端连接Linux服务器'''

# 配置选项
Host = '192.168.59.128' # Telnet服务器IP
username = 'test' # 登录用户名
password = 'abcd1234' # 登录密码
finish = ':~$ ' # 命令提示符（标识着上一条命令已执行完毕）
print '==========1======'
# 连接Telnet服务器
tn = telnetlib.Telnet(Host,port=23)
print '============2==========='
# 输入登录用户名
tn.set_debuglevel(3)
tn.read_until("login: ")
tn.write(str(username)+'\r\n')
print '=====2==========='    
# 输入登录密码
tn.read_until("Password: ")
tn.write(str(password)+'\r\n')
print '--------4----------'
tn.write('sh /home/test/hello.sh \n') 
tn.write("exit\n")
print tn.read_all()
print 'Finish!'
tn.close()
