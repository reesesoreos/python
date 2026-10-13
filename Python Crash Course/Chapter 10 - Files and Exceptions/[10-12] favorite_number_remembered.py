# Combines both parts of exercise [10-11]
import json

filename = 'fav_number.json'
path = f"outputs/{filename}"

try:
    with open(path, 'r') as f:
        favorite_number = json.load(f)

except FileNotFoundError:
    favorite_number = input("What is your favorite number? ")
    with open(path, 'w') as f:
        json.dump(favorite_number, f)
    print("Thank you. I will remember your favorite number next time.")

else:
    print(f"I know your favorite number! Your favorite number is {favorite_number}!")
