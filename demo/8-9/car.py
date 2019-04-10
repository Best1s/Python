#!/usr/bin/python3
class Car():
  def __init__(self,make,model,year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reding = 0
  def get_descriptive(self):
    long_name = str(self.year) + " " + self.make + " " + self.model
    return long_name.title()
  def update_odometer(self,mileage):
    self.odometer_reding = odometer
  def increment_odometer(self,miles):
    self.odometer_reding += miles
  def read_odometer(self):
    print("This car miles is :" + str(self.odometer_reding))
class ElectricCar(Car):
  def __init__(self,make,model,year):    
    super().__init__(make,model,year)
    self.battery = Battery()
  #def descrip_battery(self):
    #print("The car has a " + str(self.battery_size) + "-kWh battery.")  
class Battery():
  def __init__(self,battery_size = 70):
    self.battery_size = battery_size
  def descrip_battery(self):
    print("The car has a " + str(self.battery_size) + "-kWh battery.")
  def get_range(self):
    if self.battery_size == 70 :
      range = 240
    if self.battery_size == 85 :
      range = 270
    print("The cat run " + str(range) + " miles on a full charge")
  def upgrade_battery(self):
    if self.battery_size != 85:
      self.battery_size = 85    
