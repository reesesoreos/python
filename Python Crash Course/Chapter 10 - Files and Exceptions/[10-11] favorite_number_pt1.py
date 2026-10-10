import json

filename = 'fav_number.json'

favorite_number = input("What is your favorite number? ")

with open(f"outputs/{filename}", 'w') as f:
    json.dump(favorite_number, f)

