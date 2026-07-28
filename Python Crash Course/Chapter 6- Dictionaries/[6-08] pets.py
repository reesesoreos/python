pets = [
    {
        'name': 'pet 1',
        'kind of pet': 'dog', 
        'owner': 'james'
    },
    {
        'name': 'pet 2',
        'kind of pet': 'cat', 
        'owner': 'cleo'
    },
    {
        'name': 'pet 3',
        'kind of pet': 'parrot', 
        'owner': 'sam'
    }
]

for pet in pets:
    print(f"{pet['name'].title()} Information:")
    for key, value in pet.items():
        if key == 'name':
            continue
        else:   
            print(key.title())
            print(value.title())
            print()