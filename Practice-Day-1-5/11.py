#Generate a random number between 1 and 10. Ask the user to guess it.

import random

random_number = random.randint(1,10)


user_guessed_number = int(input("Guess the number:"))

if user_guessed_number == random_number:
      print("Guessed!")
else:
      print("Not guessed!")