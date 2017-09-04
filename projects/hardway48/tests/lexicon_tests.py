#!/usr/bin/python
#encoding:utf-8
from nose.tools import *
import re
print re.sub('([bcdfghjklmnpqrstvwxyz])', r'o\1', 'tobias')
# import sys
# sys.path.append("../ex48")
#注意处理方法，用shell时得换回来，不能用sys添加的方式

from ex48.ex48 import lexicon

def test_directions():
    assert_equal(lexicon.scan("north"),[('direction','north')])
    result=lexicon.scan("north south east")
    assert_equal(result,[('direction','north'),
                         ('direction', 'south'),
                         ('direction', 'east'),
                         ])

def test_verb():
    assert_equal(lexicon.scan("go"),[('ver','go')])
    result = lexicon.scan("go kill eat ")
    assert_equal(result, [('ver', 'go'),
                          ('ver', 'kill'),
                          ('ver', 'eat'),
                          ])

def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the in of ")
    assert_equal(result, [('stop', 'the'),
                          ('stop', 'in'),
                          ('stop', 'of'),
                          ])

def test_nouns():
    assert_equal(lexicon.scan('bear'), [('noun', 'bear')])
    result = lexicon.scan("bear princess ")
    assert_equal(result, [('noun', 'bear'),
                          ('noun', 'princess')
                          ])

def test_numbers():
    assert_equal(lexicon.scan('1234'), [('number', 1234)])
    result = lexicon.scan("3 91234 ")
    assert_equal(result, [('number', 3),
                          ('number', 91234)
                          ])

def test_errors():
    assert_equal(lexicon.scan('ASDFADFASDF'),[('error', 'ASDFADFASDF')])
    result=lexicon.scan("bear IAS princess")
    assert_equal(result,[('noun', 'bear'),
                          ('error', 'IAS'),
                          ('noun', 'princess'),
                          ])
