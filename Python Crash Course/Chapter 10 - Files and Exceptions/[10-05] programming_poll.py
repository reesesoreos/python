filename = 'program_reasons.txt'

while True:
    response = input("Why do you like programming? Type 'q' to quit. ")
    if response == 'q':
        break
    else:
        with open(f"outputs/{filename}", 'a') as file_object:
            file_object.write(f"{response}\n")