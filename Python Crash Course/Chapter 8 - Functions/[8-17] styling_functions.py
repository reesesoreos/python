# Exercise [8-14]

def make_car(manufacturer, model_name, **car_info):
    """Build a dictionary containing everything we know about a car."""
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model_name
    return car_info


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

# Exercise [8-13]

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile(
    'jayden',
    'park',
    location='usa',
    favorite_language='python',
    native_language='english',
)
print(user_profile)

# Exercise [8-12]

def sandwich(*sandwich_items):
    """Summarize the sandwich being made."""
    for item in sandwich_items:
        print(f"{item.title()} will be added to the sandwich.")
    print()


sandwich('roast beef', 'cheddar cheese', 'lettuce')
sandwich('turkey', 'apple slices', 'honey mustard')
sandwich('peanut butter', 'jelly')

# Added descriptive docstrings to each function definition.