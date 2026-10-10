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