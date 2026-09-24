filename = 'learning_python.txt'
with open(f"inputs/{filename}") as file_object:
    text = file_object.read()
    text = text.replace('Python', 'C')
    print(text.rstrip())