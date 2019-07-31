#!/usr/bin/python3
file_dir = "txt_file/learning_python.txt"
with open(file_dir) as file_object:
  lines = file_object.readlines()
  lines_string = ""
  print(lines[0].strip())
  print()
  for i in lines:
    lines_string += i.strip()
    print(i.rstrip())
    print(i.rstrip().replace("python","c"))
print(lines_string)
a = 0
if i in lines_string:
  a += 1
print(a)
end = 5
for i in range(0,len(lines_string)):
  end += 1
  if lines_string[i:end] == "python":
    print("on " + str(i) +" - " + str(end) + " have python")
  if end == len(lines_string):
    break