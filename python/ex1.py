#!/usr/bin/env python
#coding=utf-8
count = 0
while True:
	print_num = input('Which loop do you want it to be printed out?')
	while count < 10000000:
		if count == print_num:
			print 'There you got the number:',count
			choice = raw_input('Do you want to continue the loop?(y/n)')
 			print_num = input('Which loop do you want it to be printed out?')
			if choice == 'n':
				break
			else:
				if print_num <= count:
					print "已经过了,sx!"
			break
		else:
			print 'Loop:',count
		count +=1
	else:
		print 'loop:',count
