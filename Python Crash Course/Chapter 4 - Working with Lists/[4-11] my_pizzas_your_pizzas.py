#Reuses Exercise [4-01]
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