# #!/usr/bin/python
# #encoding:utf-8
#
# #具体见projects/hardway48
#
# stuff=raw_input('> ')
# words=stuff.split()
#
# first_word=('verb','go')
# second_word=('direction','north')
# third_word=('direction','west')
# sentence=[first_word,second_word,third_word]
#
# def convert_numbers(s):
#     try:
#         return int(s)
#     except ValueError:
#         return None
#
#
first=  ("123","123")
second= ("abc","ABC")

sentence={first,second}

def scan(sentences):
    list=[]
    words=sentences.split()
    # for i in range(len(words)):
    #     if words[i] in second:
    #         print 11111

    # for i in words:
    #     # if i.isdigit():
    #     #     print i
    #     if i in sentence:
    #         print i

scan("123 sdwhuiofhweofgio weiofhio wfrm ABC 21313143 wr43t56 54y6h7 ")

"""

PS C:\Users\Administrator> e:
PS E:\> E:\GITHUBWORK\learn-python\projects\hardway48
无法将“E:\GITHUBWORK\learn-python\projects\hardway48”项识别为 cmdlet、函数、脚本文件或可运行程序的名称。请检查名称的
拼写，如果包括路径，请确保路径正确，然后重试。
所在位置 行:1 字符: 46
+ E:\GITHUBWORK\learn-python\projects\hardway48 <<<<
    + CategoryInfo          : ObjectNotFound: (E:\GITHUBWORK\l...jects\hardway48:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS E:\> cd E:\GITHUBWORK\learn-python\projects\hardway48
PS E:\GITHUBWORK\learn-python\projects\hardway48> ls


    目录: E:\GITHUBWORK\learn-python\projects\hardway48


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----         2018/1/15     16:42            ex48
d----         2018/1/15     16:43            tests
-a---        2017/12/13     23:11        720 setup.py


PS E:\GITHUBWORK\learn-python\projects\hardway48> nosetests
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
PS E:\GITHUBWORK\learn-python\projects\hardway48>
"""

