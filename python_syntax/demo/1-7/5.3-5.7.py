#!/usr/bih/python3
import random
alien_color = "green"
if alien_color == "green":
  print("congratulation +5 score")
if alien_color == "red":
  print("+10 score")
if alien_color == "green":
  print("congratulation +5 score")
else:
  print("congratulation +10 score")
if alien_color == "green":
  print("congratulation +10 score")
elif alien_color == "yellow":
  print("congratulation +10 score")
elif alien_color == "red":
  print("congratulation +15 score")
age = random.randint(0,100)
print("age is: " + str(age))
if age < 2:
  print("baby")
elif age >=2 and age < 4:
  print("蹒跚学步")
else:
  print("old")