#!/usr/bin/python
# Learn python the hard way
# Ex16: reading and writing file

from sys import argv
from os.path import exists

#Kiem tra tham so nhap vao
while len(argv) != 2:
    print "Ban hay nhap theo dinh dang python Ex16.py tenfile"
    exit()

script, filename = argv

#Kiem tra file co ton tai
while exists(filename) == False:
    filename = raw_input("Nhap lai ten file: ")

print "Script nay se xoa noi dung file cu cua ban, hay can than!"

a = raw_input("Ban co chac chan? y/n? ")

while True:
    if a == 'y':  
        target = open(filename, 'w+')
        # Xoa noi dung file cu
        target.truncate()
        break
    elif a == 'n':
        exit()
    else:
        a = raw_input("Ban co chac chan? y/n? ")

#Nhap noi dung file moi

sodong = int(raw_input("Nhap vao so dong cua file moi: "))

for i in range (1, sodong + 1):
    print ("Nhap vao noi dung dong so %d: ") %i
    target.write(raw_input("\t>"))
    target.write("\n")
    
#print target.read()
    
target.close()