#!/usr/bin/python
# encoding:utf-8
from nose.tools import *
import nose
import sys
# sys.path.append("..\\")
sys.path.append("../ex48")
#注意路径
from ex48 import lexicon
#在家里win10的64位上正常，单位win7的32位powershell,折腾半天查找到原因是没有把hardway48下面的__init__.py删掉造成的，
# 删掉后powershell瞬间正常...注意基础，出问题了要多尝试，多角度看问题，注意对比...到是查清了__init__.py的用法。

def text_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("north South EAST west dOwn up left right back")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'South'),
                          ('direction', 'EAST'),
                          ('direction', 'west'),
                          ('direction', 'dOwn'),
                          ('direction', 'up'),
                          ('direction', 'left'),
                          ('direction', 'right'),
                          ('direction', 'back')
                          ])


def test_verbs():
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicon.scan("go KILL eat stop")
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'KILL'),
                          ('verb', 'eat'),
                          ('verb', 'stop')
                          ])


def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the in of FROM at it")
    assert_equal(result, [('stop', 'the'),
                          ('stop', 'in'),
                          ('stop', 'of'),
                          ('stop', 'FROM'),
                          ('stop', 'at'),
                          ('stop', 'it'),
                          ])


def test_numbers():
    assert_equal(lexicon.scan("1234"), [('number', '1234')])
    result = lexicon.scan("3 91234 23098 8128 0")
    assert_equal(result, [('number', '3'),
                          ('number', '91234'),
                          ('number', '23098'),
                          ('number', '8128'),
                          ('number', '0'),
                          ])


def test_errors():
    assert_equal(lexicon.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
    result = lexicon.scan("Bear IAS princess")
    assert_equal(result, [('noun', 'Bear'),
                          ('error', 'IAS'),
                          ('noun', 'princess')
                          ])