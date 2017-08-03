#!/usr/bin/python
#encoding:utf-8

from sys import argv
from  os.path import exists

script,from_file,to_file=argv

print "copy from %s to %s"%(from_file,to_file)

in_file=open(from_file)
indata=in_file.read()

print "the input file is %d bytes long "%len(indata)

print "does the output file exist?%r"%exists(to_file)
print "ready,hit return to continue,control+c to abort."
raw_input()

out_file=open(to_file,'w')
out_file.write(indata)

print "done"

out_file.close()
in_file.close()

"""
$ cat test.txt 这个是LINUX里面的指令

Microsoft Windows [版本 6.1.7601]
版权所有 (c) 2009 Microsoft Corporation。保留所有权利。

C:\Users\Administrator>cd E:/GITHUBWORK/learn-python/hardway

C:\Users\Administrator>e:

E:\GITHUBWORK\learn-python\hardway>python hardway17.py test.txt new_file.txt
copy from test.txt to new_file.txt
the input file is 49 bytes long
does the output file exist?False
ready,hit return to continue,control+c to abort.

done

"""