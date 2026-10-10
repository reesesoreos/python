buffet_foods = ('fried rice', 'chicken', 'steak', 'sushi', 'potatoes')
for food in buffet_foods:
    print(f"The buffet offers {food}.")

# Intentional function that would result in an error: 
# buffet_foods[0] = ("rice"). This was asked for in the exercise.

buffet_foods = ('orange chicken', 'tacos', 'steak', 'sushi', 'potatoes')
for food in buffet_foods:
    print(f"The buffet offers {food}.")


# This reuses the foods.py examples shown in the book.
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(f"{food.title()}")

print("My friend's favorite foods are:")
for food in friend_foods:
    print(f"{food.title()}")


# Reuses Exercise [4-01]
pizza_types = ['pepperoni', 'cheese', 'hawaiian']
for pizza in pizza_types:
    print(f"I really like {pizza.title()} pizza.")

print("I really love pizza.")

friend_pizzas = pizza_types[:]
pizza_types.append('barbecue')
friend_pizzas.append('mushroom')

for pizza in pizza_types:
    print(f"My favorite pizzas are {pizza.title()}.")

for pizza in friend_pizzas:
    print(f"My friend's favorite pizzas are {pizza.title()}.")

# This reuses exercises [4-11], [4-12], [4-13].