#!/usr/local/bin/python3
pizzas = ("dicss","kfc","vir")
for pizza in pizzas:
  print(pizza)
for value in range(1,11):
  print(value,end="")
print(end="\n")
print("test")
value = []
for i in range(1,11):
  value.append(2**i)
  print(value[i-1],end="\t")
  print("test")
print(min(value))
print(max(value))
print(sum(value))
value = [2**value for value in range(1,11)]
print(value)
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[1:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)