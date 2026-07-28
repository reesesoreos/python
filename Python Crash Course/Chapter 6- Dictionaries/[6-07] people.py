people = [
    {'first_name' : 'brenden', 'last_name' : 'park', 'age' : 17, 'city' : 'los angeles'},
    {'first_name' : 'jayden', 'last_name' : 'park', 'age' : 15, 'city' : 'los angeles'},
    {'first_name' : 'james', 'last_name' : 'smith', 'age' : 19, 'city' : 'san francisco'},
    ]

for person in people:
    print(f"First name: {person['first_name'].title()}")
    print(f"Last name: {person['last_name'].title()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].title()}")
    print()