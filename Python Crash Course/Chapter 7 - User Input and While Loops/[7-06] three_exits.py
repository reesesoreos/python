# Reuses and modifies exercise [7-04]
# Original version, uses 'break'
while True:
    topping = (input("Please choose a topping to put on your pizza. "))
    if topping == 'quit':
        break
    else:
        print(f"I will add {topping} to your pizza.")

# Version 2, uses conditional test
topping = ""

while topping != 'quit':
    topping = input("Please choose a topping to put on your pizza. Type 'quit'" \
    "to end.")

    if topping != 'quit':
        print(f"I will add {topping} to the pizza.")

# Version 3, uses active variable
active = True
while active:
    topping = (input("Please choose a topping to put on your pizza. "))
    if topping == 'quit':
        active = False
    else:
        print(f"I will add {topping} to your pizza.")