#!/usr/bin/env python
# _*_ coding:utf-8 _*_

def countAge(yson,setAge,yfater):
	differAge = (int)(setAge - yson)
	realFatherAge = (int)(yfater + differAge)
	return realFatherAge
print countAge(5,7,26)
