sandwich_orders = [
    'tuna sandwich', 
    'steak sandwich', 
    'pulled pork sandwich',
     'fried chicken sandwich']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)

print("I have made all of the following sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich.title())