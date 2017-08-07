#!/usr/bin/python
# encoding:utf-8

def break_words(stuff):
    """break up"""
    words=stuff.split()
    #words = stuff.split(' ')
    return  words
"""
遇到问题'list' object has no attribute 'split'
"""

def sort_words(words):
    """sort words"""
    return sorted(words)

def print_first_words(words):
    """print_first_words after poping"""
    word=words.pop(0)
    print word

def print_last_words(words):
    """print_last_words after poping"""
    word =words.pop(-1)
    print words

def sort_sentence(sentence):
    """sort sentence"""
    words=break_words(sentence)
    print sort_words(words)

def print_first_and_last(sentence):
    """print_first_and_last words in sentence"""
    words=break_words(sentence)
    print_first_words(words)
    print_last_words(words)

def print_first_and_last_sorted(sentence):
    """print_first_and_last_sorted in sentence"""
    words=sort_sentence(sentence)
    print_first_words(words)
    print_last_words(words)

# Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (
# Intel)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import hardway25
# >>> sentence="uyhiyh jhuiohn mnom omo "
# >>> words=hardway.break_words(sentence)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'hardway' is not defined
# >>> words=hardway25.break_words(sentence)
# >>> words
# ['uyhiyh', 'jhuiohn', 'mnom', 'omo', '']
# >>> sorted_words=hardway25.sort_words(words)
# >>> sorted_words
# ['', 'jhuiohn', 'mnom', 'omo', 'uyhiyh']
# >>>
# >>> hardway25.print_first_word(words)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'module' object has no attribute 'print_first_word'
# >>> hardway25.print_first_words(words)
# uyhiyh
# >>> hardway25.break_words(sentence)
# ['uyhiyh', 'jhuiohn', 'mnom', 'omo', '']
# >>> help(ex25
# ... help(ex25)
#   File "<stdin>", line 2
#     help(ex25)
#        ^
# SyntaxError: invalid syntax
# >>> help(ex25)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'ex25' is not defined
# >>> help(hardway25)
# Help on module hardway25:
#
# NAME
#     hardway25
#
# FILE
#     d:\python\python27\hardway25.pyc
#
# FUNCTIONS
#     break_words(stuff)
#         break up
#
#     print_first_and_last(sentence)
#         print_first_and_last words in sentence
#
#     print_first_and_last_sorted(sentence)
#         print_first_and_last_sorted in sentence
#
#     print_first_words(words)
#         print_first_words after poping
#
#     print_last_words(words)
#         print_last_words after poping
#
# -- More  --

