#!/usr/bin/python

# Ex15: readfile

from sys import argv

if len(argv) != 2:
    print '''This programe require 1 argument!
Ban hay nhap vao ten file can doc!'''
    exit()
else:
    print "Doc noi dung tu file", argv[1]

for i in open(argv[1]).readlines():
    print '.' * len(i)
    print i
    