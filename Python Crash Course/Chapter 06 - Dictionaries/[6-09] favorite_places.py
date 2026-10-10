favorite_places = {
    'james' : ['korea', 'japan', 'china'],
    'john' : ['canada'],
    'jacob' : ['brazil', 'argentina'],
}
for key, value in favorite_places.items():
    for country in value:
        print(f"{key.title()}'s favorite place is {country.title()}.")
        print()