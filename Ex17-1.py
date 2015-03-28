#!/usr/bin/python
# Learn python the hard way
# Ex16: more about file
# Chuong trinh doc du lieu tu mot file va dem so lan xuat hien cua cac tu, cac ky tu trong file
# ghi ket qua ra file khac

from sys import argv
from os.path import exists


while len(argv) != 3:
    print 'Ban hay nhap dung dinh dang "python Ex17.py file_nguon file_ketqua"'
    exit()

print "\nChuong trinh dem so lan xuat hien cua cac tu, cac ky tu trong mot file"
    
script, file_source, file_dest = argv

if exists(file_source) == False:
    print "Khong ton tai file nguon!"
    exit()
else:
    in_file = open(file_source, 'r')
    in_data = in_file.read()
    
    #Chia noi dung file thanh cac tu, day vao list_word
    list_word = in_data.split()
    dict_data = {}
    for i in list_word:
        if i in dict_data:
            dict_data[i] = dict_data [i] + 1
        else:
            dict_data[i] = 1
    
    #Ghi noi dung ket qua vao file
    if exists(file_dest) == False:
        print "File dich khong ton tai. Tao file moi! Press Enter or Ctr + C"
        raw_input()
        out_file = open(file_dest,'w')
    else:    
        print "Ghi ket qua sang %s!" %file_dest
        out_file = open(file_dest,'w')
    out_file.writelines("Dem so luong tu co trong %s\n" %file_source)
    for key in dict_data:
        a = "  - Tu '%s' xuat hien %d lan." %(key,dict_data[key])
        out_file.writelines(a + '\n')


    #Chia noi dung file thanh cac ky tu, day vao list_char
    list_char = list(in_data)
    dict_char = {}
    
    #Dem so lan xuat hien cua ky tu bang dictionary
    for i in list_char:
        if i in dict_char:
            dict_char[i] = dict_char [i] + 1
        else:
            dict_char[i] = 1
            
    #Ghi ket qua vao file dich 
#    out_file = open(file_dest,'w')
    out_file.writelines("\nDem so luong ky tu co trong %s\n" %file_source)
    for key in dict_char:
        if key == '\n':
            out_file.writelines(  "  - Ky tu 'Enter' xuat hien %d lan.\n" %dict_char[key])
        else:
            a = "  - Ky tu '%s' xuat hien %d lan." %(key,dict_char[key])
            out_file.writelines(a + '\n')
            
    print "Done!"

in_file.close()
out_file.close()
print "\nXem noi dung cua file %s de biet ket qua" %file_dest
