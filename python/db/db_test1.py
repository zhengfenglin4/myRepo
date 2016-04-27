#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def print_db(db):
	for k,v in db.iteritems():
        	print k,v
import dbhash
db=dbhash.open('db-test','c')
db['zfl']='郑锋林'
db['qzj']='邱志娟'
db['zyx']='郑宇轩'
print '---------------'
print_db(db)
if db.has_key('zfl'):
	del db['zfl']
print '======================del zfl'
print_db(db)
db.close()
