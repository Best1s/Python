#!/usr/bin/python3
f_num = input("fist num :")
l_num = input("2nd num :")
try :
  sum1 = int(f_num) + int(l_num)
  print(sum1)
except ValueError:
  print ("plase input num")
  while True:
    sum1 = 0
    f_num = input("fist num :")
    l_num = input("2nd num :")
    try :
      sum1 = int(f_num) + int(l_num)
      print(sum1)
    except ValueError:
        print ("plase input num")
    