class User():
  def __init__(self,f_name,l_name,age,sex,login_attempts=0):
    self.f_name=f_name
    self.l_name=l_name
    self.age=age
    self.sex=sex
    self.login_attempts = login_attempts
  def describe_user(self):
    info = self.f_name  + " " + self.l_name + " " + self.age + " " + self.sex + \
    " login day is: "+ str(self.login_attempts)
    #info = [self.f_name,self.l_name,self.age,self.sex]
    print(info)
  def greet_user(self):
    print(self.f_name + self.l_name +" "+ "very good !")
  def increment_login_attempts(self):
    self.login_attempts += 1
  def reset_login_attempts(self):
    self.login_attempts = 0