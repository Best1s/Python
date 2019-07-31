from user import User
from privileges import Privileges
class Admin_User(User):
  def __init__(self,f_name,l_name,age,sex,login_attempts=0):
    super().__init__(f_name,l_name,age,sex,login_attempts=0)    
    self.privileges = Privileges()