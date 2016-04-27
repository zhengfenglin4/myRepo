#!/usr/bin/env python
# _*_ coding:utf-8 _*_
zf = raw_input('输入您要查询鲜花的名称:')
sjs = ['长春花','珍珠花','向日葵','风铃草','金盏菊','含羞草','夹竹桃','大丽花']
#enumerate可对对列，数组，字符串遍历
for index,sj in enumerate(sjs):
	if zf in sj:
		print sj
