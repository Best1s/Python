#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# copy file 
#with open('/path/to/some/file/you/want/to/read') as file_1, \
#    open('/path/to/some/file/being/written', 'w') as file_2:
#    file_2.write(file_1.read())
from sys import argv
from os.path import exists
script, from_file, to_file = argv 
in_file = open(from_file)
indata = in_file.read()
if exists(to_file):
  print "begin copy text to %s" % to_file
else:
  print to_file,"is not exist,begin create"
out_file = open(to_file,"w")
out_file.write(indata)
out_file.close()
in_file.close() 