car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("Is car == 'audi'? I predict False.")
print(car == 'audi')

print()

computer = 'MacBook'
print("Is computer.lower() == 'MacBook'? I predict False.")
print(computer.lower() == 'MacBook')
print("Is computer.lower() == 'macbook'? I Predict True.")
print(computer.lower() == 'macbook')

print()

number = 5
print("Is number > 3? I predict True.")
print(number > 3)
print("Is number < 2? I predict False.")
print(number < 2)
print("Is number != 5? I predict False.")
print(number != 5)
print("Is number >= 5? I predict True.")
print(number >= 5)

print()

age = 20
gender = 'male'
print("Over age 18 and male? I predict True.")
print(age > 18 and gender == 'male')
print("Over age 23 and male? I predict False.")
print(age > 23 and gender == 'male')

print()

print("Over age 30 or male? I predict True.")
print(age > 30 or gender == 'male')
print("Under age 18 or female? I predict False.")
print(age < 18 or gender == 'female')

print()

names_list = ['james', 'john', 'anthony']


print("Is 'james' in names_list? I predict True.")
print('james' in names_list)

print("Is 'jacob' in names_list? I predict False.")
print('jacob' in names_list)

print("Is 'jacob' not in names_list? I predict True.")
print('jacob' not in names_list)

print("Is 'john' not in names_list? I predict False.")
print('john' not in names_list)
