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
    
restaurant1 = Restaurant('panda express', 'chinese')

restaurant2 = Restaurant('taco bell', 'mexican')

restaurant3 = Restaurant('mcdonalds', 'american')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
