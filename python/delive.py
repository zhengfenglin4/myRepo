#!/usr/bin/env python
#coding=utf-8
import re
import sys
sys.path.append(r'tools')
import read_config_line
def deliver(config,actions,selfAction=''):
	global COUNT
	print '==================================='
	print 'stemp %s Deliver activities' % COUNT
	COUNT = COUNT + 1
	if(selfAction == '' and actions == ''):
		allAction = ''
	elif(actions == ''):
		allAction = selfAction
	elif(selfAction == ''):
		allAction = actions
	else:
		allActions = actions + ',' + selfAction
	if(allActions == ''):
		print 'no action need to be deliver'
		print 'system exit'
		return True,0
	tn = None
	global FINISH
	host = config['Hostname']
	username = config['Username']
	password = config['Password']
	localHost = config['LocalHost']
	finish = remote + FINISH
	#try:
	#	tn = MyTelnet(host,username,password)
	#	if tn:

#def main():
args = sys.argv
ACTIONS = re.sub(r'\s','',args[1]).split(':',1)[1]
print ACTIONS
#	allConfig = read_config_line.readConfig()
#	deliverOK = False
#	flag = 0
#	admin = allConfig['admin-user']
#	print admin
	#actions = ACTIONS
	#print read_config_line.printDict(admin)
	#try:
	#	deliverOK,flag = deliver(admin,actions)
#allConfig = read_config_line.readConfig()
#admin = allConfig['admin-user']
#print admin
