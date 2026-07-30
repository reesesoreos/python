# Reuses exercise [6-02]
favorite_numbers = {
    'james' : [3, 5, 10], 
    'john' : [73, 33, 21], 
    'ethan' : [44, 222, 108], 
    'jacob' : [98, 33], 
    'greg' : [23, 11],
}
for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(number)
    print()