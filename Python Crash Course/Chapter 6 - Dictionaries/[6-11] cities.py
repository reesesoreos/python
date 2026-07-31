cities = {
    'los angeles' : 
        {'country' : 'USA', 
         'population' : 3870000, 
            'fact' : 'the city was founded in 1781'},

    'sacramento' : 
        {'country' : 'USA',
          'state' : 'california',
            'population' : 538750},
    
    'san francisco' : 
        {'country' : 'USA', 
         'state' : 'california', 
         'population' : 826000},
}

for city, information in cities.items():
    print(f"{city.title()} Information:")
    for key, value in information.items():
        print(f"{key.title()}:")
        print(value)
        print()