print("Please give two numbers, and I will add them.")
number1 = input("Please give the first number. ")
number2 = input("Please give the second number. ")

try:
    int1 = int(number1)
    int2 = int(number2)

except ValueError:
    print("Please enter a numerical value such as 5 instead of 'five'.")

else:
    print(int1 + int2)