import random

health = 50

difficulty = random.randint(1,3)

potion_health = random.randint(25,50) // difficulty

health = health + potion_health

print('Difficulty:', difficulty, '\nHealth before:', health - potion_health, '\nAfter potion:', health)