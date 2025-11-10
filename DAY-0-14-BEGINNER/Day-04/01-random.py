# Importing the random module
import random

# -----------------------------------------------
# 1️⃣ GENERATE RANDOM NUMBERS
# -----------------------------------------------

# Random float between 0 and 1
print("Random float between 0 and 1:", random.random())

# Random integer between 1 and 10 (inclusive)
print("Random integer between 1 and 10:", random.randint(1, 10))

# Random number from range 0 to 20 with step of 2
print("Random even number between 0 and 20:", random.randrange(0, 20, 2))

# Random floating-point number between 5 and 10
print("Random float between 5 and 10:", random.uniform(5, 10))


# -----------------------------------------------
# 2️⃣ RANDOM CHOICE AND SELECTION
# -----------------------------------------------

colors = ["red", "green", "blue", "yellow", "black", "white"]

# Random single choice from list
print("Random color (single choice):", random.choice(colors))

# Random multiple choices (with repetition)
print("Random 3 colors (can repeat):", random.choices(colors, k=3))

# Random sample (without repetition)
print("Random 2 unique colors:", random.sample(colors, 2))


# -----------------------------------------------
# 3️⃣ SHUFFLE A LIST
# -----------------------------------------------

numbers = [1, 2, 3, 4, 5, 6]
print("\nOriginal list:", numbers)
random.shuffle(numbers)
print("Shuffled list:", numbers)


# -----------------------------------------------
# 4️⃣ USING SEED (REPRODUCIBLE RANDOMNESS)
# -----------------------------------------------

# Same seed gives same random results every time
random.seed(42)
print("\nRandom number with seed 42:", random.randint(1, 100))

random.seed(42)
print("Same random number again with seed 42:", random.randint(1, 100))


# -----------------------------------------------
# 5️⃣ SMALL PROGRAM EXAMPLES
# -----------------------------------------------

# Example 1: Pick a random winner from a list
names = ["Alice", "Bob", "Charlie", "Daisy"]
winner = random.choice(names)
print("\n🎉 The winner is:", winner)

# Example 2: Random password generator (simple)
characters = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"
password = "".join(random.sample(characters, 8))  # 8-char random password
print("Generated password:", password)

# Example 3: Dice roll simulator
dice = random.randint(1, 6)
print("🎲 You rolled a:", dice)
