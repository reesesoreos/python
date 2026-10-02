filename = 'cats.txt'

try:
    with open(f"inputs/{filename}") as file:
        words = file.read()

except FileNotFoundError:
    print(f"{filename} is missing.")

else:
    print(words)

print()

filename = 'dogs.txt'

try:
    with open(f"inputs/{filename}") as file:
        words = file.read()

except FileNotFoundError:
    print(f"{filename} is missing.")

else:
    print(words)