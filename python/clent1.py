#!/usr/bin/env pytho
"""
anuthor:   zhengfenglin
  Purpose: 
  Created: 2016/2/17
"""
import socket,select,string,sys
def prompt():
    sys.stdout.write('<You>')
    sys.stdout.flush()

if __name__ == '__main__':
    #if(len(sys.argv)<3):
    #    print 'Usage:python %s hostname port'%sys.argv[0]
    #    sys.exit()
    #host = sys.argv[1]
    #port = int(sys.argv[2])
    host = 'localhost'
    port = 5000
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(2)
    s.connect((host,port))
    print 'Connect to remote host.Start sending message'
    prompt()
    while True:
        rlist = [sys.stdin,s]
        read_list,write_list,error_list = select.select(rlist, [],[])
        for sock in read_list:
            if sock == s:
                data = sock.recv(4096)
                if not data:
                    print '\nDisconnected from chat server'
                    sys.exit()
                else:
                    sys.stdout.write(data)
                    prompt()
            else:
                msg = sys.stdin.readline()
                s.send(msg)
                prompt()

