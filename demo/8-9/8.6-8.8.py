#!/usr/bin/python3
def city_country(local,city):
  a = {local:city}
  return a
def make_album(**stat_info):
  stat = {}
  for key,vlues in stat_info.items():
    stat
  return stat
b = city_country("shanghai","china")
print(b)
b = city_country("beijing","china")
print(b)
b = city_country("shandong","china")
print(b)
#disk = {}
i =0
while True:
  i = i + 1
  name = input("plase input name:")
  song = input("plase input song:")
  disk = make_album(name,song) 
  a = input("input 'q' quit ")
  if a == "q":
    break
print(disk)
