def sandwich(*sandwich_items):
    for item in sandwich_items:
        print(f"{item.title()} will be added to the sandwich.")
    print()

sandwich('roast beef', 'cheddar cheese', 'lettuce')
sandwich('turkey', 'apple slices', 'honey mustard')
sandwich('peanut butter', 'jelly')