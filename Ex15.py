#!/usr/bin/python

# Ex15: readfile

from sys import argv
from os.path import exists

if len(argv) != 2:
    print '''This programe require 1 argument!
Ban hay nhap vao ten file can doc!'''
    exit()
else:
    print "Doc noi dung tu file", argv[1]
    print open(argv[1]).read()

file2 = raw_input("Nhap ten file thu 2 can doc: ")
print "File so 2 co ton tai? %s" %exists(file2)
print "Doc noi dung tu file", file2
print open(file2).read()
print "Do dai file thu 2 la %d bytes" %len(open(file2).read())