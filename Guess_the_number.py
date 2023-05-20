''' 
Guess the number game is a game where the computer picks a random number between 1 and 100
and the user has to guess the number. The computer will tell the user if their guess is too high or too low.
The user will have 10 guesses to guess the number correctly. If the user guesses the number correctly
within 10 guesses, they win. If they don't guess the number correctly within 10 guesses, they lose.
'''

import random

print("Welcome to the Guess the Number Game!")
print("The computer will pick a random number between 1 and 100 and you will have 10 guesses to guess the number correctly.")
print("If you guess the number correctly within 10 guesses, you win. If you don't guess the number correctly within 10 guesses, you lose.")

# computer picks a random number between 1 and 100
computer_number = random.randint(1, 100)

# user guesses the number
user_guess = input("Please guess a number between 1 and 100: ")

# check if user input is a number
while not user_guess.isdigit():
    user_guess = input("Please guess a number between 1 and 100: ")

# convert user input to integer
user_guess = int(user_guess)

# check if user input is between 1 and 100
while user_guess < 1 or user_guess > 100:
    user_guess = input("Please guess a number between 1 and 100: ")
    while not user_guess.isdigit():
        user_guess = input("Please guess a number between 1 and 100: ")
    user_guess = int(user_guess)

# check if user guessed the number correctly
if user_guess == computer_number:
    print("You guessed the number correctly! You win!")
else:
    print("You didn't guess the number correctly. You lose.")
    print("The number was", computer_number)

# check if user guessed the number correctly within 10 guesses
for i in range(1, 10):
    if user_guess == computer_number:
        print("You guessed the number correctly within 10 guesses! You win!")
        break
    else:
        user_guess = input("Please guess a number between 1 and 100: ")
        while not user_guess.isdigit():
            user_guess = input("Please guess a number between 1 and 100: ")
        user_guess = int(user_guess)
        if user_guess == computer_number:
            print("You guessed the number correctly within 10 guesses! You win!")
            break
        elif i == 9:
            print("You didn't guess the number correctly within 10 guesses. You lose.")
            print("The number was", computer_number)
            break
        else:
            continue

# check if user wants to play again
play_again = input("Would you like to play again? (Y/N): ")

while play_again != "Y" and play_again != "N":
    play_again = input("Would you like to play again? (Y/N): ")

if play_again == "Y":
    print("Welcome to the Guess the Number Game!")
    print("The computer will pick a random number between 1 and 100 and you will have 10 guesses to guess the number correctly.")
    print("If you guess the number correctly within 10 guesses, you win. If you don't guess the number correctly within 10 guesses, you lose.")
    computer_number = random.randint(1, 100)
    user_guess = input("Please guess a number between 1 and 100: ")
    while not user_guess.isdigit():
        user_guess = input("Please guess a number between 1 and 100: ")
    user_guess = int(user_guess)
    while user_guess < 1 or user_guess > 100:
        user_guess = input("Please guess a number between 1 and 100: ")
        while not user_guess.isdigit():
            user_guess = input("Please guess a number between 1 and 100: ")
        user_guess = int(user_guess)
    if user_guess == computer_number:
        print("You guessed the number correctly! You win!")
    else:
        print("You didn't guess the number correctly. You lose.")
        print("The number was", computer_number)
    for i in range(1, 10):
        if user_guess == computer_number:
            print("You guessed the number correctly within 10 guesses! You win!")
            break
        else:
            user_guess = input("Please guess a number between 1 and 100: ")
            while not user_guess.isdigit():
                user_guess = input("Please guess a number between 1 and 100: ")
            user_guess = int(user_guess)
            if user_guess == computer_number:
                print("You guessed the number correctly within 10 guesses! You win!")
                break
            elif i == 9:
                print("You didn't guess the number correctly within 10 guesses. You lose.")
                print("The number was", computer_number)
                break
            else:
                continue
else:
    print("Thanks for playing!")
    exit()

