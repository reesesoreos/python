def count_words(filename):
    with open(f"inputs/{filename}") as f:
        text = f.read()
        number_the = text.lower().count('the ')
        print(f'The word "the" is mentioned {number_the} times.')

count_words('pride_and_prejudice.txt')
count_words('the_odyssey.txt')
count_words('romeo_and_juliet.txt')