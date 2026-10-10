number = int(input("Please give me a number, and I will tell you if it is a " \
"multiple of 10. "))

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")

else:
    print(f"{number} is not a multiple of 10.")