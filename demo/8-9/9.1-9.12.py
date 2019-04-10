#!/usr/bin/python3
#from car import Car,ElectricCar,Battery
''' from module_name import * '''
import car
from restaurant import * 
from admin import *
class Son_User(User):
  def __init__(self,f_name,l_name,age,sex,login_attempts):
    super().__init__(f_name,l_name,age,sex,login_attempts)

my_res = Restaurant("meat","eat" )
my_res.open_restaurant()
my_res.set_number_served(20)
my_res.describe_restaurant()
my_res.increment_number_served(10)

my_ice = IceCreamStand("Green-ice","ice")
my_ice.add_falavors("hot")
my_ice.describe_ice()

my_user = User("wang","chunying","18","man",22)
my_user.increment_login_attempts()
my_user.describe_user()
my_user.reset_login_attempts()
my_user.describe_user()
my_user.greet_user()

my_son_usr = Son_User("ma","haojie","18","man",11)
my_son_usr.describe_user()

my_admin = Admin_User("Bani","zhang","18","man")
#my_admin.show_privileges()
my_admin.privileges.add_privileges("ban user")
my_admin.privileges.show_privileges()

my_tesla = car.ElectricCar("tesla","model s",2019)
print(my_tesla.get_descriptive())
my_tesla.battery.descrip_battery()
my_tesla.battery.get_range()

my_new_tesla = car.ElectricCar("new_tesla","model s",2019)
my_new_tesla.battery.upgrade_battery()
my_new_tesla.battery.get_range()