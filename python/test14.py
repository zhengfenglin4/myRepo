#!/usr/bin/env python
#!/usr/bin/python
#coding:utf-8


import sys
sys.stderr = open('/dev/null')       # Silence silly warnings from paramiko
import paramiko as pm
sys.stderr = sys.__stderr__
import os


class AllowAllKeys(pm.MissingHostKeyPolicy):
   def missing_host_key(self, client, hostname, key):
       return


HOST = '192.168.5.130'
USER = 'wls81'
PASSWORD = 'Paic#234'


client = pm.SSHClient()
client.load_system_host_keys()
#client.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
client.set_missing_host_key_policy(AllowAllKeys())
client.connect(HOST, username=USER, password=PASSWORD)


channel = client.invoke_shell()
stdin = channel.makefile('wb')
stdout = channel.makefile('rb')


stdin.write('''
ls -lrt  /wls/jbossserver/jboss-as-7.1.1.Final/standalone/deployments/mbp-web.war
df /wls | grep /wls
top -b -n 1 | head -n 5
exit
''')
#文件写入
file_object = open('file.txt', 'w')
file_object.write(stdout.read())
file_object.close( )
#print stdout.read()

stdout.close()
stdin.close()
client.close()
