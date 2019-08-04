# GuessingGame.py
# Billy Ridgeway
# A number guessing game.

import random   # Imports the random module.

the_number = random.randint(1, 10)  # Create a variable and generates a random number
                                    # between 1 and 10.

# Asks the user to guess a number between 1 and 10 and stores the number in the variable guess.
guess = int(input("Guess a number between 1 and 10: "))

# Creates a while loop to evaluate the user's guess.
while guess != the_number:
    if guess > the_number:
        print(guess, "was too high. Try again.")
    if guess < the_number:
        print(guess, "was too low. Try again.")
    guess = int(input("Guess again: "))
print(guess, "was the number! You win!")
    
    
    
