#!/usr/bin'python3
i = ""
#try:
#  with open("aa.txt","a") as file_object1:
#    fdasfas = file_object1.read()
#except FileNotFoundError:
#  print("not file")
with open("guest.txt","a") as file_object:
  file_object.write("Haojie,nice to meet you.\n")
  file_object.write("Chunying is so cool.\n")
  user_name = input("Plase input name: ")
  while True:
    great_name = "Hello " + user_name + ",nice to meet you!\n"
    print(great_name)
    file_object.write(great_name)
    print("Enter 'q' to quit ")
    user_name = input("Plase input name: ")
    if user_name == "q":
      break

    