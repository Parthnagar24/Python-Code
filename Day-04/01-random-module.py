# Random module demonstration

import random

# Generate a random integer btw 1 and 10 (inclusive)
random_integer = random.randint(1,10)
print(random_integer)

# Generate a random float btw 0 and 1 (exclusive)
random_float = random.random()
print(random_float)

# Generate a random float btw 0 and 5 (exclusive)
random_float = random.random() * 5
print(random_float)

# Generate a random float between 1 and 10
random_float = random.uniform(1, 10)
print(random_float)


#Simulate coin toss

random_heads_or_tails =random.randint(0,1)
if random_heads_or_tails == 1:
    print("Heads")
else:
    print("Tails")