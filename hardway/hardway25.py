#!/usr/bin/python
# encoding:utf-8

def break_words(stuff):
    """break up"""
    words=stuff.split(' ')
    return  words

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