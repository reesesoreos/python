def city_country(city, country):
    return(f"{city.title()}, {country.title()}")

place1 = city_country('paris', 'france')
place2 = city_country('tokyo', 'japan')
place3 = city_country('new york city', 'united states')

print(place1)
print(place2)
print(place3)