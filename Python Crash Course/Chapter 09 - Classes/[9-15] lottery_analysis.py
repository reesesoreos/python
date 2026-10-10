# Reuses [9-14]

from random import choice


my_ticket = ['e', 2, 6, 'a']

count = 0
active = True


while active:
    lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
    winning_tickets = []
    count += 1

    for value in range(1,5):
        win = choice(lottery)
        lottery.remove(win)
        winning_tickets.append(win)
    
    
    if my_ticket == winning_tickets:
        print("You have won the lottery!")
        print(f"It took {count} attempts.")
        active = False
    
    else:
        continue
