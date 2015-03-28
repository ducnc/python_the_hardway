#!/usr/bin/python
# Learn python the hard way
# Ex16: more about file

from sys import argv
from os.path import exists


while len(argv) != 3:
    print 'Ban hay nhap dung dinh dang "python Ex17.py file_nguon file_dich"'
    exit()

print "\nChuong trinh nhap doc du lieu tu mot file va write ra mot file khac"
    
script, file_source, file_dest = argv

if exists(file_source) == False:
    print "Khong ton tai file nguon!"
else:
    in_file = open(file_source, 'r')
    in_data = in_file.read()
    print "Kich thuoc file nguon la: ", len(in_data)

if exists(file_dest) == False:
    print "File dich khong ton tai. Tao file moi! Press Enter or Ctr + C"
    raw_input()
else:    
    print "Chep noi dung file_nguon sang file_dich!"
try:    
    out_file = open(file_dest,'w')
    out_file.write(in_data)
    print "Done!"
except Exception, e:
    print e
    
in_file.close()
out_file.close()