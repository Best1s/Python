class Restaurant():
  def __init__(self,restaurant_name,cuisine_type):
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    self.number_served = 0
  def describe_restaurant(self):
    print("The restaurant is " + self.restaurant_name + " The type is " + self.cuisine_type )
    print("Porson is count " + str(self.number_served))
  def open_restaurant(self):
    print("Restaurant is open")
  def set_number_served(self,serve):
     self.number_served = serve
  def increment_number_served(self,serve):
    self.number_served += serve
    print("Tody server porson is  " + str(serve) + " Porson  is count: " + str(self.number_served))
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)        
        self.flavors = ["milk","salt","lemmo","red"]
    def add_falavors(self,flavors):
        self.flavors.append(flavors)
    def describe_ice(self):
        print("The ice stone flavors is", end=" : ")   
        #print(self.flavors)
        for i in self.flavors:
            print("\t" + i ,end="")
        print()