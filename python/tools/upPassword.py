#!/usr/bin/env python
#coding=utf-8
import sys
class update():
	def updatePassword(self):
		message = ""
		oldPwd = raw_input("请输入原始密码:")
		if (oldPwd == 'python'):
			newPwd = raw_input('请输入新密码:')
			if(len(newPwd) > 6) and (len(newPwd) < 18):
				renewPwd=raw_input('请输入确认密码:')
				if(renewPwd!=newPwd):
					message='两次输入的密码不一致,修改失败!'
				else:
					message='恭喜你！密码修改成功！'
			else:
				message='密码长度必须在6-18位之间'
		else:
			message = '原始密码输入错误,请重新输入!'
		return message
	def checkName(self):
		i = 0
		while i<=3:
        		name = raw_input('输入你的用户名:')
        		i = i + 1
        		if name == 'zfl':
                		print updatePassword()
				break
			else:
				if i == 3:
					sys.exit('输入用户次数过多，程序将退出！')
				else:
					print '用户输入错误,请重新输入'
				continue
	def printName(self,name):
		print name
if __name__ == '__main__':
	update().checkName()
