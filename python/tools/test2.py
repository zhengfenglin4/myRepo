import getpass 
import sys 
import telnetlib 
HOST = "192.168.59.128"
user = raw_input("Enter your remote account:") 
password = getpass.getpass() 
tn = telnetlib.Telnet(HOST) 
tn.read_until("login: ") 
tn.write(str(user) + "\n") 
if password:   
	tn.read_until("Password: ")   
	tn.write(str(password) + "\n") 
tn.write("ls\n") 
tn.write("exit\n") 
print tn.read_all() 

