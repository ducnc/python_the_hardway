#!/usr/bin/python

from sys import argv

prom = '\t> '

if len(argv) != 2:
    print "This programe require 1 argument!"
    exit()
else:
    print "Hello, I'm %s script of %s" %(argv[0], argv[1])

print "Please write your name!"

a = raw_input(prom)

print "Please write your age!"

b = raw_input(prom)

print "So, you are %s and you're %s" %(a, b)