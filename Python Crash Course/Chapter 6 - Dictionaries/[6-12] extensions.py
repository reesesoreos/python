# The original code is from the Python Crash Course book, pg. 110 - 111. 
# I have added some new lines and labeled them with comments for the exercise.

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        'field' : 'physics',    # New
        'born' : 1879,  # New
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        'field' : 'chemistry', # New
        'born' : 1867,  # New
    },
    'inewton' : {   # New
        'first' : 'isaac',
        'last' : 'newton',
        'location' : 'london',
        'field' : 'mathematics',    
        'born' : 1643,  

    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    field = user_info['field']  # New
    born = user_info['born']    # New
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
    print(f"\tField: {field.title()}")  # New
    print(f"\tBorn: {born}")    # New
