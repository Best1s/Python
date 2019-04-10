#!/usr/bin/python3
def make_album(**stat_info):
  stat = {}
  for key,vlue in stat_info.items():
    stat[key] = vlue
  return stat
name = input("plase input name:")
song = input("plase input song:")
disk = make_album(name = song , name1 = 'song2')
#a = input("input 'q' quit ")
#if a == "q":
#    break
print(disk)