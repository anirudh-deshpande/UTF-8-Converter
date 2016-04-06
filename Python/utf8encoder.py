#__author__ = 'Anirudh'

#Notes
    #Take care of big endian
    #unichar
    #convert from Character ti Hex
    #sys.setdefaultencoding("utf-8")





import codecs
file="C:\Users\Anirudh\PycharmProjects\NLPAssignments\english_in.txt"
source = codecs.open(file,"r","utf-16-be")
destination = codecs.open("utf8encoder_out.txt","wb","utf-8")
contents=source.read()
destination.write(contents)


#from sys import argv
#script, file = argv
# import codecs
# file="C:\Users\Anirudh\PycharmProjects\NLPAssignments\gujarati_in.txt"
# source = codecs.open(file,"r","utf-16-be")
# destination = codecs.open("utf8encoder_out.txt","w","utf-8")
#
# BLOCKSIZE = 1048576
#
# while True:
#     contents=source.read(1048576)
#     if not contents:
#         break
#     destination.write(contents)

# byte=f.read()
# print byte
# utf16 = byte.decode('utf-16')
# utf8 = utf16.encode('utf-8')
# print utf8
# output.write(utf8)


#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Shivankur Kapoor
#
# Created:
# Copyright:   (c) Shivankur Kapoor
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# import sys
# UTF16Stream =[]
# reload(sys)
# sys.setdefaultencoding('UTF-8')
#
# def decode(w1):
#
#     a = int("".join(map(lambda x: '%02x' % ord(x), w1)),16)
#
#     return a
#
#
#
# fr = open(sys.argv[1],'rb')
# ##fw = open('C:\\Users\\Shivankur Kapoor\\Desktop   \\USC\\SEM 2\\NLP\\Assignment 1\\english_out.txt','w')
#
# try:
#     byte = fr.read(1)
#     while byte:
#         ##print byte
#         UTF16Stream.append(byte)
#         byte = fr.read(1)
#
# ##    for i,k in zip(UTF16Stream[0::2], UTF16Stream[1::2]):
#     for x in UTF16Stream:
#          print unichr(decode(x))
# #    print '\xE6\x97\xA5'
#
#
#          ##fw.write(char)
#
# finally:
#     fr.close()
#     ##fw.close()