#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import shelve
db=shelve.open('db-test')
db['zfl']=['郑锋林','18916902079','江西','28']
db['qzj']=['邱志娟','18321685922','江西','29']
db['zyx']=['郑宇轩','18321685822','江西','1']
for d in db['zfl']:
	print d
db.close()
