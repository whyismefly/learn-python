#!/usr/bin/python
# encoding:utf-8

"""
PS C:\Users\Administrator> cd E:\learn\GitHub\learn-python\hardway\projects\hardway51\gothonweb
PS E:\learn\GitHub\learn-python\hardway\projects\hardway51\gothonweb> python bin/app.py
http://0.0.0.0:8080/
127.0.0.1:50121 - - [04/Mar/2019 01:06:03] "HTTP/1.1 GET /" - 404 Not Found
127.0.0.1:50121 - - [04/Mar/2019 01:06:03] "HTTP/1.1 GET /favicon.ico" - 404 Not Found
127.0.0.1:50121 - - [04/Mar/2019 01:06:10] "HTTP/1.1 GET /hello" - 200 OK
127.0.0.1:50172 - - [04/Mar/2019 01:07:21] "HTTP/1.1 GET /hello" - 200 OK
127.0.0.1:50254 - - [04/Mar/2019 01:15:39] "HTTP/1.1 GET /hello" - 200 OK
127.0.0.1:50254 - - [04/Mar/2019 01:15:44] "HTTP/1.1 POST /hello" - 200 OK
127.0.0.1:50315 - - [04/Mar/2019 01:21:11] "HTTP/1.1 GET /hello" - 200 OK
127.0.0.1:50315 - - [04/Mar/2019 01:21:16] "HTTP/1.1 GET /hello" - 200 OK
127.0.0.1:50410 - - [04/Mar/2019 01:27:04] "HTTP/1.1 GET /hello" - 200 OK
127.0.0.1:50410 - - [04/Mar/2019 01:27:08] "HTTP/1.1 GET /" - 404 Not Found
127.0.0.1:50460 - - [04/Mar/2019 01:27:40] "HTTP/1.1 GET /hello" - 200 OK127.0.0.1:50469 - - [04/Mar/2019 01:27:44] "HTTP/1.1 GET /hello" - 200 OK

127.0.0.1:50583 - - [04/Mar/2019 01:32:20] "HTTP/1.1 GET /" - 404 Not Found
127.0.0.1:50537 - - [04/Mar/2019 01:32:20] "HTTP/1.1 GET /hello" - 200 OK127.0.0.1:50567 - - [04/Mar/2019 01:32:20] "HTTP/1.1 GET /hello" - 200 OK

127.0.0.1:50600 - - [04/Mar/2019 01:32:34] "HTTP/1.1 GET /" - 404 Not Found
127.0.0.1:50610 - - [04/Mar/2019 01:32:49] "HTTP/1.1 POST /hello" - 200 OK
"""

"""
PS C:\Users\Administrator> cd E:\learn\GitHub\learn-python\hardway\projects\hardway51\gothonweb
PS E:\learn\GitHub\learn-python\hardway\projects\hardway51\gothonweb> nosetests
.
----------------------------------------------------------------------
Ran 1 test in 0.544s

OK
PS E:\learn\GitHub\learn-python\hardway\projects\hardway51\gothonweb>
"""