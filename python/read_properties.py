#!/usr/bin/env python 
#encoding=UTF-8
import re

def readConfig(filename='time.ini'):
    datas = {}
    data = None
    with open(filename) as config:
        lines = config.readlines()
    for line in lines:
        line=re.sub(r'$\s','',line)
        if line.startswith('#') or line == '' : continue
        if line.startswith('[') and line.endswith(']'):
            data = line[1:-1]
            datas[data]={}
        else:
            if re.search(r'=', line):
                item=line.split('=',1)
                key=item[0]
                value=item[1]
                if data:
                    datas[data][key]=value
            else:
                #print datas[data][line]
                #datas[data][line]=''
                pass
    return datas

#test print
def printDict(datas):
    for (key, value) in datas.items():
        print '['+key+']'
        for (subkey, subvalue) in value.items():
            print subkey+'='+subvalue


if __name__ == '__main__':
    printDict(readConfig('test.ini'))
    #printDict(readConfig('../time.ini'))
