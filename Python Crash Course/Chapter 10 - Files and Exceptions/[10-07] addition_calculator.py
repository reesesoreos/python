# Reuses exercise [10-06]


while True:
    print("Please give two numbers, and I will add them. Type 'q' at any time to quit the program.")
    number1 = input("Please give the first number. ")

    if number1 == 'q':
        break

    number2 = input("Please give the second number. ")

    if number2 == 'q':
        break

    try:
        int1 = int(number1)
        int2 = int(number2)

    except ValueError:
        print("Please enter a numerical value such as 5 instead of 'five'.")
        print()

    else:
        print(int1+int2)