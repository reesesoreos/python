# Reuses exercise [9-01] 

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant's name is {self.restaurant_name.title()}.")
        print(f"The cuisine type of the restaurant is {self.cuisine_type.title()}.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open.")

    def set_number_served(self, number_served):
        self.number_served = number_served
        
    
    def increment_number_served(self, increment):
        self.number_served += increment
        

restaurant = Restaurant('panda express', 'chinese')


print(restaurant.number_served)
restaurant.set_number_served(5)
print(restaurant.number_served)
restaurant.increment_number_served(10)
print(restaurant.number_served)