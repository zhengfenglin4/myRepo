#coding:utf-8
import ConfigParser
parser = ConfigParser.ConfigParser()
fname='test.ini'
print parser.read(fname)
print '*' * 20
sects = parser.sections()
print sects
print '*' * 20
print parser.options(sects[0])
print '*' * 20
print parser.items(sects[0])
print '*' * 20
print parser.get(sects[0],'user')
#添加数据
parser.add_section('info')
parser.set('info','user','python')
parser.set('info','pwd','python')
parser.set('info','port','23')
parser.write(open('test.ini','w'))
