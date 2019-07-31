#!/usr/bin/python
for i in range(1,21):
  print(i,end="\t")
print()
value = [i for i in range(1,100001)]
print(len(value))
print(min(value))
print(max(value))
print(sum(value))
value = (i for i in range(1,21,2))
for i in value:
    print(i,end="\t")
value = (i for i in range(3,31,3))
print()
for i in value:
    print(i,end="\t")
value = (i for i in range(3,31))
print()
for i in value:
    if i%3 == 0:
        print(i,end="\t")
value = (i**3 for i in range(1,11))
print()
for i in value:
    print(i,end="\t")