dinner_list = ['george washington', 'benjamin franklin', 'abraham lincoln']
print(f"Hello, {dinner_list[0].title()}, I would like to invite you to dinner.")
print(f"Hello, {dinner_list[1].title()}, I would like to invite you to dinner.")
print(f"Hello, {dinner_list[2].title()}, I would like to invite you to dinner.")

print(f"Hello {dinner_list[0].title()}, {dinner_list[1].title()}, and {dinner_list[2].title()}, we have found a bigger dinner table. More people will be invited.")
dinner_list.insert(0, 'alexander hamilton')
dinner_list.insert(2, 'john adams')
dinner_list.append('franklin roosevelt')

print(f"Hello, {dinner_list[0].title()}, I would like to invite you to dinner with some others.")
print(f"Hello, {dinner_list[1].title()}, I would like to invite you to dinner with some others.")
print(f"Hello, {dinner_list[2].title()}, I would like to invite you to dinner with some others.")
print(f"Hello, {dinner_list[3].title()}, I would like to invite you to dinner with some others.")
print(f"Hello, {dinner_list[4].title()}, I would like to invite you to dinner with some others.")
print(f"Hello, {dinner_list[5].title()}, I would like to invite you to dinner with some others.")

print("Unfortunately, I can only invite two people for dinner. ")
removed_1 = dinner_list.pop()
print(f"Sorry {removed_1.title()}, I cannot invite you to dinner this time.")
removed_2 = dinner_list.pop()
print(f"Sorry {removed_2.title()}, I cannot invite you to dinner this time.")
removed_3 = dinner_list.pop()
print(f"Sorry {removed_3.title()}, I cannot invite you to dinner this time.")
removed_4 = dinner_list.pop()
print(f"Sorry {removed_4.title()}, I cannot invite you to dinner this time.")

print(f"{dinner_list[0].title()}, {dinner_list[1].title()}, you guys are still invited to dinner.")
del dinner_list[0]
del dinner_list[0]
print(dinner_list)