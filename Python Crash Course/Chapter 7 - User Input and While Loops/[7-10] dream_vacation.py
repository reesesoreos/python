active = True
poll = {}
while active:
    name = input("What is your name? ")
    location = input("If you could visit anywhere, where would you go?" \
    " Type 'quit' to stop the program. ")
    
    if location == 'quit':
        active = False
    else:
        poll[name] = location
        
print("All the results are in, and these are the results:")
for key, value in poll.items():
    print(f"{key.title()} would like to go to {value.title()}.")