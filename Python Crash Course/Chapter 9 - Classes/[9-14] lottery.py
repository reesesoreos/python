from random import choice

lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

for value in range(1,5):
    win = choice(lottery)
    lottery.remove(win)
    print(f"{win} is one of the winning tickets.")