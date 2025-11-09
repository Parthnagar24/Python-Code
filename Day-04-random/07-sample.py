import random

numbers = [1, 2, 3, 4]
sampled = random.sample(numbers, 2)

print("Sampled elements:", sampled)
print("Original list remains:", numbers)
#Returns a list of n unique elements (without replacement)