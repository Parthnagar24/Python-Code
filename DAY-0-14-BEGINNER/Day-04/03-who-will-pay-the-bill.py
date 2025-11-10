# 🎯 Banker Roulette Game
# Randomly selects one person who will pay the bill

import random

# List of friends
friends = ['A', 'B', 'C', 'D', 'E']

# Randomly choose one friend to pay the bill
#random.choice() is a built-in method in Python’s random module that selects one random item from a non-empty sequence like a list, tuple, or string.


random_friend =random.choice(friends)
print(random_friend + " is going to buy the meal today!")