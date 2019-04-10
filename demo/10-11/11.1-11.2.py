#!/usr/bin/python3
import unittest
class Test_cities(unittest.TestCase):
  def test_city_function(self):
    info = city_function("guangzhou","china")
    self.assertEqual(city_function,"Guangzhou,China")
def city_function(city,country):
  city_info = city.title() + "," + country.title()
  return city_info
print(city_function("sahnghai","china"))
print(city_function("Guangzhou","China"))
unittest.main()