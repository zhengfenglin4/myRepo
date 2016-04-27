#!/usr/bin/env python
#-*- coding: utf-8 -*-  
import paramiko  
import os
var=123 
os.environ['var']=str(var)
os.system('echo $var') 
