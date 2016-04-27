#!/usr/bin/env python
#coding:utf-8
"""
  Author:   zhengfenglin
  Purpose: 
  Created: 2016/2/17
"""
import select
import socket
def broadcast_data(sock,message):
    for socket in CONNECTION_LIST:
        if socket != server and socket !=sock:
            socket.send(message)
            socket.close()
            CONNECTION_LIST.remove(socket)
if __name__ == '__main__':
    CONNECTION_LIST = []
    outputs =[]
    PORT = 5000
    RECV_BUFFER = 4096
    timeout=10
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('localhost',PORT))
    server.listen(10)
    CONNECTION_LIST.append(server)
    print 'Chat server started on port ' + str(PORT)
    while True:
        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,outputs,CONNECTION_LIST,timeout)
        #print 'read_sockets:',read_sockets
        #print 'CONNECTION_LIST:',CONNECTION_LIST        
        if not (read_sockets or write_sockets or error_sockets):
            print '等待客户端接入...'
            continue
        else:
            for sock in read_sockets:
                #print 'sock:',sock
                #print 'server:',server
                if sock == server:
                    sockfd,addr=server.accept()
                    CONNECTION_LIST.append(sockfd)
                    print 'client (%s,%s)connected' %addr
                    broadcast_data(sockfd, '[%s:%s] entered room\r' %addr)
                else:
                    data = sock.recv(RECV_BUFFER)
                    print data
                    broadcast_data(sock, "\r"+'<' +str(sock.getpeername())+'>'+data)
