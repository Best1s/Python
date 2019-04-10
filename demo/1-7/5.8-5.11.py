#!/usr/bin/python3
user = ["admin","dabai","xiaohei","xiaohong","2dog"]
for i in user:
  if i == "admin":
    print("Hello " + i + ", would you like to see a status report?")
  else:
    print("Hello " + i + ", thank you for logging in again")
user = []
if len(user) == 0:
  print("We need to find some users!")
else:
  for i in user:
    if i == "admin":
      print("Hello " + i + ", would you like to see a status report?")
    else:
      print("Hello " + i + ", thank you for logging in again")
print()
current_users = ["admin","dabai","xiaohei","xiaohong","2dog"]
new_users = ["2dog","xiaobai","xiaohong","apple"]
for new_user in new_users:
  if new_user.lower() in current_users:
    print("The " + new_user + " alread use,please change")
  else:
    print("The "+ new_user + " ok!")
value = [i for i in range(1,10)]
for i in value:
  if i == 1:
    print("1st")
  elif i == 2:
    print("2nd")
  else:
    print(str(i) + "th")