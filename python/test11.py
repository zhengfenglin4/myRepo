#!/usr/bin/env python
#-*- coding: utf-8 -*-  
import paramiko  
import threading  
         
hostname='192.168.179.130'
username='test'
password='abcd1234'
         
#port=22    
if __name__=='__main__':    
        paramiko.util.log_to_file('paramiko.log')    
        s=paramiko.SSHClient()    
        #s.load_system_host_keys()    
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())    
        s.connect(hostname = hostname,username=username, password=password)    
        stdin,stdout,stderr=s.exec_command('ifconfig;free;df -h')    
        print stdout.read()    
        s.close()
