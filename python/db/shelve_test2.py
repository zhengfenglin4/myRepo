#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import shelve
class Person:
	def __init__(self,title,content):
		self.title = title
		self.content = content
	def say(self):
		print '您输入的标题是:%s\t您输入的内容是:%s' %(self.title,self.content)
temppath = 'MyGood'
def init():
	m = {}
	f = shelve.open(temppath)
	f['init'] = '---------------欢迎您使用万能记事本-----------------------'
	f.close()
init()
print '请选择您的下一步:\n(add) 添加永久保存的内容\t(del)删除永久的内容\t(quit)关闭记事本\n(show)展示永久保存的内容\t(say)展示不保存的内容'
while(True):
	f = shelve.open(temppath)
	check=raw_input('选择您下一步的操作:')
	if check == 'quit':
		break
	if check == 'add':
		print '---------------欢迎您使用添加主题功能-----------------------'
		titleSave = raw_input('请输入您想永久保存的标题:')
		contentSave = raw_input('请输入您要永久保存的内容:')
		f['title'] = titleSave
		f['content'] = contentSave
		print '我添加的标题是:'+f['title'],'我添加的内容是:'+f['content']
	if check == 'del':
		print '---------------欢迎您使用删除主题功能-----------------------'
		titleDel = raw_input('请输入您想删除标题的键值:')
		if f.has_key(titleDel):
			del f[titleDel]
		print '删除成功'
	if check == 'say':
		titleSave = raw_input('请输入您想永久保存的标题:')
                contentSave = raw_input('请输入您要永久保存的:')
		p = Person(titleSave,contentSave)
		p.say()
		print '仔细看清楚啊，我没有保存哦'
	if check == 'show':
		print '---------------下面是您永久保存的内容-----------------------'
		for key,value in f.iteritems():
			print '',value
		print '--------------------over-----------------------------------'
	f.close()
