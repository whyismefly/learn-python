#!/usr/bin/python
#encoding:utf-8

#具体见projects/hardway48

stuff=raw_input('> ')
words=stuff.split()

first_word=('verb','go')
second_word=('direction','north')
third_word=('direction','west')
sentence=[first_word,second_word,third_word]

def convert_numbers(s):
    try:
        return int(s)
    except ValueError:
        return None


