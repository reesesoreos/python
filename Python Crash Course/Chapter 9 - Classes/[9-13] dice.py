from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1,self.sides))


die6 = Die()
print("10 rolls for the 6 sided die:")
for number in range(1,11):
    die6.roll_die()

print()

die10 = Die(10)
print("10 rolls for the 10 sided die:")
for number in range(1,11):
    die10.roll_die()

print()

die20 = Die(20)
print("10 rolls for the 20 sided die:")
for number in range(1,11):
    die20.roll_die()