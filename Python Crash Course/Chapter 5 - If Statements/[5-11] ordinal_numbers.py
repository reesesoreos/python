numbers_list = list(range (1,10))
if numbers_list:
    for number in numbers_list:
        if number == 1:
            print(f"{number}st \n")
        elif number == 2:
            print(f"{number}nd \n")
        elif number == 3:
            print(f"{number}rd \n")
        else:
            print(f"{number}th \n")