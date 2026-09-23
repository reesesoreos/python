filename = 'learning_python.txt'
with open(f"inputs/{filename}") as file_object:
    text = file_object.read()
    print(text.rstrip())

print()

with open(f"inputs/{filename}") as file_object:
    for line in file_object:
        print(line.rstrip())

print()

with open(f"inputs/{filename}") as file_object:    
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
    
