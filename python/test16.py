#!/usr/bin/env python
# -*- coding=utf-8 -*-
"""
Usage:
Just A Template
"""
from __future__ import division
 
import sys,time
j = '#'
if __name__ == '__main__':
    for i in range(1,61):
        j += '#'
	sys.stdout.write(str(int((i/60)*100)) + "\r")
        #sys.stdout.write(str(int((i/60)*100))+'%  ||'+j+'->'+"\r")
        sys.stdout.flush()
        time.sleep(0.5)
print
