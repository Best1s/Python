import json 
def get_stored_username(): 
  """ 如果存储了用户名，就获取它 """ 
  filename = 'username.json' 
  try: 
    with open(filename) as f_obj: 
      username = json.load(f_obj) 
  except FileNotFoundError: 
    return None 
  else: 
    return username
def get_new_username():
  ''' 新用户名'''  
  username = input("What is your name? ") 
  filename = 'username.json'
  with open(filename, 'w') as f_obj: 
      json.dump(username, f_obj)
  return username
def update_username(name):
  '''update username'''
  filename = 'username.json'
  with open(filename,"w") as f_obj:
    json.dump(name,f_obj)
def greet_user(): 
  """问候用户，并指出其名字""" 
  username = get_stored_username()
  if username: 
    print("Welcome back, " + username + "!") 
  else:    
    username = get_new_username()
    print("We'll remember you when you come back, " + username + "!") 
greet_user()
yes_no = input("The name is yes?(y/n)")
if yes_no == "n":
  username = input("What is your name? ")
  update_username(username)
  greet_user()