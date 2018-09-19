# coding=utf-8
import sys

str = '什么?'

type = sys.getfilesystemencoding()
str = str.decode("UTF-8").encode(type)

print str
str = str.replace('<','').replace('>','').replace('/','').replace('\\','').replace('|','').replace(':','').replace('\"','').replace('\*','').replace('?','')
print str
