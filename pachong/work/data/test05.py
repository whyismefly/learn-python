# !/usr/bin/python
# -*- coding: UTF-8 -*-
import os
def job1_goon():
    print "11111111111111111111111111111111"
    while True:
        info=raw_input("more:")
        if info == "s":
            print info, "再续一会"
            os.system("shutdown -a")
        else:
            print "as plan"

job1_goon()