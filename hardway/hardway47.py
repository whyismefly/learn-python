#!/usr/bin/python
# encoding:utf-8
"""具体见project/hardway47"""

"""
Windows PowerShell
版权所有 (C) 2009 Microsoft Corporation。保留所有权利。

PS C:\Users\Administrator> cd e
Set-Location : 找不到路径“C:\Users\Administrator\e”，因为该路径不存在。
所在位置 行:1 字符: 3
+ cd <<<<  e
    + CategoryInfo          : ObjectNotFound: (C:\Users\Administrator\e:String) [Set-Location], ItemNotFoundException
    + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.SetLocationCommand

PS C:\Users\Administrator> cd e:
PS E:\> cd E:\GITHUBWORK\learn-python\projects\hardway47
PS E:\GITHUBWORK\learn-python\projects\hardway47> ls


    目录: E:\GITHUBWORK\learn-python\projects\hardway47


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----        2017/12/13     23:11            ex47
d----        2017/12/13     23:11            tests
-a---        2017/12/13     23:11        719 setup.py


PS E:\GITHUBWORK\learn-python\projects\hardway47> nosetests
...
----------------------------------------------------------------------
Ran 3 tests in 0.005s

OK

"""