#!/usr/bin/env python
#_*_ coding:utf-8  _*_
import subprocess
'''
retcode = subprocess.call(['ls','-l'])
print retcode
'''

retcode = subprocess.call("ls -l",shell=True)
