# Uses user_profile.py from the book.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

print(
    build_profile(
    'jayden', 
    'park', 
    location='usa', 
    favorite_language = 'python',
    native_language = 'english',)
    )