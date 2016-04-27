#!/usr/bin/env python
#_*_ coding:utf-8 _*_

'''
¿¿:
   --¿¿¿¿¿¿
   --¿¿¿¿¿¿¿¿¿¿¿
   --¿¿¿¿¿¿¿

'''
import sys
retty_limit = 3
retty_count = 0
account_file = 'accounts.txt'
lock_file = 'account_lock.txt'
while retty_count < retty_limit:
	username = raw_input('\033[32;lm;username;\033[0m')
	lock_check = file(lock_file)
	
	for line in lock_check.readlines():
		if username == line.split()[0]:
			sys.exit('\033[31;1m;user %s is locked!;\033[0m' % username)
	password =  raw_input('\033[32;lm;password;\033[0m')
	f = file(account_file,'rb')
	match_flag = False
	for line in f.readlines():
		user,passwd = line.strip('\n').split()
		if username == user and password == passwd:
			print 'Match!',username
			match_flag = True
			break
	f.close()
	if match_flag == False:
		print 'User unmatched!'
		retty_count +=1
	else:
		print 'Welcome login OldBoy Learning system!'
else:
	print 'Your account is locked!'
	f = file(lock_file,'ab')
	f.write(username + '\n')
	f.close()
