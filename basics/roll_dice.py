import random

roll = random.randint(1, 6)

guess = int(input('Guess dice roll: '))

if roll == guess:
    print('Correct ' + str(roll))
else:
    print('Wrong ' + str(roll))