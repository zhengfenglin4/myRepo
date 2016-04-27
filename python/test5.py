#!/usr/bin/env python
#-*-coding:utf-8-*-  
import threading
import paramiko
import os,sys
import time
class SSHThread(threading.Thread):
	def __init__(self,host_ip,username,passwd,command):
		threading.Thread.__init__(self)
		self.host_ip = host_ip
		self.username = username
		self.passwd = passwd
		self.command = command
	def run(self):
		host_ip = self.host_ip	
		username = self.username
		passwd = self.passwd
		command = self.command
		
		ssh = paramiko.SSHClient()
		ssh.load_system_host_keys()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	
