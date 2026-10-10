active = True

while active:
    age = input("How old are you? Type 'quit' to end the program. ")

    if age == 'quit':
        active = False
    
    else:
        if int(age) < 3:
            price = 0
        elif int(age) <= 12:
            price = 10
        else:
            price = 15
        

        print(f"Your movie ticket costs {price} dollars.")