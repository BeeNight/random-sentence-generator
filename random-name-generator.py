name = ['Sam', 'Abby', 'Max', 'Lee']
verb = ['kicks', 'runs', 'rides', 'buys']
noun = ['lion', 'plane', 'zebra', 'bicycle']
from random import randint
def pick(words):
    num_words = len(words)
    num_picked = randint(0, num_words - 1)
    word_picked = words[num_picked]
    return word_picked

while True:
    print(pick(name), pick(verb), 'a', pick(noun), end='.')
    input()

