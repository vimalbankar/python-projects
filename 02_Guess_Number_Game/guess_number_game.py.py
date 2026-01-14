# Random Number Guessing Game
# The computer generates a random number
# The user tries to guess the number

import random  # Import random module to generate random numbers


# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)

attempts = 0  # Variable to count number of guesses

print("Welcome to the Random Number Guessing Game!")
print("I have selected a number between 1 and 20.")
print("Try to guess it!\n")


# Loop until the correct number is guessed
while True:
    # Take user input
    guess = input("Enter your guess: ")

    # Check if input is a number
    if not guess.isdigit():
        print("Please enter a valid number.\n")
        continue  # Go back to start of loop

    guess = int(guess)  # Convert input to integer
    attempts += 1       # Increase attempt count

    # Check if guess is correct
    if guess == secret_number:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break  # Exit loop when guessed correctly

    # If guess is too low
    elif guess < secret_number:
        print("Too low! Try again.\n")

    # If guess is too high
    else:
        print("Too high! Try again.\n")
