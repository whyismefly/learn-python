#!/usr/bin/python
# encoding:utf-8

formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
print formatter % (
    "啦啦啦",
    "123423whquidiqp3的方法维吾尔",
    "But it didn't sing.",
    "So I said goodnight."
)

formatter2 = "%s %s %s %s"
print formatter2 % (
    "啦啦啦",
    "123423whquidiqp3的方法维吾尔",
    "But it didn't sing.",
    "So I said goodnight."
)