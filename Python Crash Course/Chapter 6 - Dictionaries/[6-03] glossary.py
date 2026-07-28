glossary = {
    'list' : 'collection of items in a variable',
    'for loop' : 'a loop that repeats a block of code',
    'if statement' : 'a statement that evaluates a condition',
    'if-else statement' : 'statement that runs certain code based on its '
    'conditional value', 
    'if-elif-else chain' : 'chain that checks multiple statements'}

for definition in glossary:
    print(f"{definition.title()}:")
    print(glossary[definition])
    print()