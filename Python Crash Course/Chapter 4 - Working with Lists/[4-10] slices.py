#This reuses exercise [4-07]
multiples = list(range(3, 33, 3))
for value in multiples:
    print(value)

print(f"The first three items in the list are: {multiples[0:3]}")
print(f"Three items from the middle of the list are: {multiples[4:7]}")
print(f"The last three items from the list are: {multiples[-3:]} ")