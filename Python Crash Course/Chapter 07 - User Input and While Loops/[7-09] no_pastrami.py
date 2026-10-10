sandwich_orders = [
    'tuna sandwich', 
    'steak sandwich', 
    'pastrami sandwich',
    'pulled pork sandwich',
     'fried chicken sandwich',
     'spicy chicken sandwich',
     'pastrami sandwich',
     'pork cutlet sandwich',
     'barbecue sandwich',
     'short rib sandwich',
     'pastrami sandwich',
]

finished_sandwiches = []

print("The deli has run out of pastrami sandwiches.")

while 'pastrami sandwich' in sandwich_orders:
        sandwich_orders.remove('pastrami sandwich')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
   
    print(f"I made your {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)

print("I have made all of the following sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich.title())