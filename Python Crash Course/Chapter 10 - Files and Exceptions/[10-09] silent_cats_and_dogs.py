# Reuses exercise [10-08]

filename = 'cats.txt'

try:
    with open(f"inputs/{filename}") as file:
        words = file.read()

except FileNotFoundError:
    pass

else:
    print(words)

print()

filename = 'dogs.txt'

try:
    with open(f"inputs/{filename}") as file:
        words = file.read()

except FileNotFoundError:
    pass

else:
    print(words)