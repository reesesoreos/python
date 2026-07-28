# This uses the favorite languages code provided in page 97.
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

poll_people = ['edward', 'john', 'james', 'sarah', 'nancy']
for person in poll_people:
    if person in favorite_languages:
        print(f"{person.title()}, thank you for responding to the poll.")
    else:
        print(f"{person.title()}, please respond to the poll.")