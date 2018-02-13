#!/usr/bin/python
# encoding:utf-8

import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def gethtml(url):
    page =urllib.urlopen(url)