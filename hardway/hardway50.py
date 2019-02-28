# #!/usr/bin/python
# #encoding:utf-8

"""mkdir bin NAME tests docs在powershell中会报错，得一个一个mkdir
"""

"""
PS C:\Users\Administrator> cd E:\learn\GitHub\learn-python\hardway\projects\hardway50\gothonweb
PS E:\learn\GitHub\learn-python\hardway\projects\hardway50\gothonweb> ls


    目录: E:\learn\GitHub\learn-python\hardway\projects\hardway50\gothonweb


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----         2019/3/1      1:13                bin
d-----         2019/3/1      1:05                docs
d-----         2019/3/1      1:06                gothonweb
d-----         2019/3/1      1:05                templates
d-----         2019/3/1      1:09                tests


PS E:\learn\GitHub\learn-python\hardway\projects\hardway50\gothonweb> python bin/app.py
http://0.0.0.0:8080/
127.0.0.1:50855 - - [01/Mar/2019 01:15:41] "HTTP/1.1 GET /" - 200 OK
127.0.0.1:50855 - - [01/Mar/2019 01:15:44] "HTTP/1.1 GET /" - 200 OK
"""