# Reuses exercise [9-01]

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"The restaurant's name is {self.restaurant_name.title()}.")
        print(f"The cuisine type of the restaurant is {self.cuisine_type.title()}.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open.")
    
restaurant = Restaurant('panda express', 'chinese')

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['strawberry', 'vanilla', 'chocolate']
    
    def display_flavors(self):
        print(self.flavors)

ice_cream_stand = IceCreamStand('baskin robbins', 'ice cream')
ice_cream_stand.display_flavors()