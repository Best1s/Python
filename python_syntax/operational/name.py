
with open ("bbb","r") as rf:
  out_file = open("a","w")
  for lines in rf.readlines():
    lines = str(lines).split()
    #print type(line)
    for line in lines:
      if line[-1] == ":" or line == "server_name" or line == ";":
        continue
      if line[-1] == ";":
        line = line[:-1]
      print line
      #line = line + "\n"
      #out_file.write(line)
  #out_file.close()