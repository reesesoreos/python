response = input("What is your name? ")
filename = 'guest.txt'

with open(f"outputs/{filename}", 'w') as file_object:
    file_object.write(response)