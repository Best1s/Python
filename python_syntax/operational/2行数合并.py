#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import argv

def read_file(read_file,out_file,need_merge_line):
  sum = 0
  with open (read_file,"r") as read_file:
    out_file = open(out_file,"w")
    for line in read_file.readlines():
      sum += 1
      line = line.ljust(30, "+")
      if sum%need_merge_line != 0:
        line = line.rstrip() + "\t"
        #if sum%1 == 0 and len(line) < 10:
          #line = line + " "*(20-len(line)) + "\t"
        #elif sum%2 == 0 and len(line) < 32:
        #  line = line.ljust(20)
        #  line = line + " "*2*(50-len(line))
        #print(sum)
      out_file.write(line)
    out_file.close()

def main():
  try:
    script, s_file, out_file, need_merge_line = argv
  except ValueError:
    script,s_file, out_file = argv
    need_merge_line = 2
  while True:
    try:
      need_merge_line=int(need_merge_line)
    except ValueError:
      need_merge_line = input("Please input merge line:")
    else:
      print("")
      break
  read_file(s_file,out_file,need_merge_line)

if __name__ == '__main__':
  main()  

