#!/usr/bin/python3
dog = {"type":"cute","master":"join"}
cat = {"type":"small","master":"jimi"}
pets = [dog,cat]
for pet in pets:
  print(pet)
favorite_places = {
  "dabai":["sahnghai","beijing"],
  "xiaohong":["zhejiang"],
  "2dog":["shenzhen","beijing"]
}
for name,places in favorite_places.items():
  print(name + " is favorite ")
  for place in places:
    print ("\t" + place)
cities = {
  "上海":{
    "country":"china",
    "population":"7666w"
  },
  "河南":{
    "country":"china",
    "population":"10000w"
  },
  "广州":{
    "country":"china",
    "population":"8888w"
  }
}
for citi,infos in cities.items():
  print(citi + " info is :")
  for info,value in infos.items():
    print("\t" + info + " :" + value)