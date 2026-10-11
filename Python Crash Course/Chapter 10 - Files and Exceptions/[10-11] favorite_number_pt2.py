import json

filename = 'fav_number.json'

with open(f"outputs/{filename}", 'r') as f:
    favorite_number = json.load(f)
    print(f"I know your favorite number! It's {favorite_number}!")