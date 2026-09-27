filename = 'guest_book.txt'

while True:
    name = input("What is your name? Type 'q' to quit the program. ")
    if name == 'q':
        break

    else:
        print(f"Welcome, {name.title()}. You've been added to the guest book.")
        with open(f"outputs/{filename}", 'a') as file_object:
            file_object.write(f"{name}\n")