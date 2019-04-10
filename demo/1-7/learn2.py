#!/usr/bin/python3
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = "1"
while message != 'quit':
  message = input(prompt)
print(message)