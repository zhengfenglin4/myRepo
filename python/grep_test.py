#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import re
log = open('paramiko.log','r+')
logbak = open('paramikobak.log','w')
count = 0
for s in log.readlines():
	li = re.findall('paramiko',s)
	if li:
		count = count + li.count('paramiko')
		s = s.replace('paramiko','paramiko.www.baidu.com')
	logbak.write(s)
log.close()
logbak.close()
