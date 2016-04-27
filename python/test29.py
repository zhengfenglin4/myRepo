#!/usr/bin/env python
s = ''
for i in range(1,10):
	for j in range(1,i+1):
		s = s + "%d * %d = %d\t" %(j,i,i*j)
	print s + '\n'
	s = ''

