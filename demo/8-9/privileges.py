class Privileges():
  def __init__(self,privileges=[]):
    self.privileges = ["Manage_user","add_user","change_passwd","change_info"]
  def add_privileges(self,add):
    self.privileges.append(add)
  def show_privileges(self):
      print(self.privileges)