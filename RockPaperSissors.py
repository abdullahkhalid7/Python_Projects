import random

print("Welcome to Rock, Paper, Scissors!")

user_choice = input("""
Please choose one of the following:\n
1. Rock
2. Paper
3. Scissors
Enter your choice:""")

while (user_choice != "1" and user_choice != "2" and user_choice != "3"):
    user_choice = input("""
    Please choose one of the following:\n
    1. Rock
    2. Paper
    3. Scissors
    Enter your choice:""")

user_choice = int(user_choice)

computer_choice = random.randint(1, 3)
set = {1: "Rock", 2: "Paper", 3: "Scissors"}
print("You have chosen", set[user_choice])
print("The computer has chosen", set[computer_choice])

if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == 1:
    if computer_choice == 2:
        print("You lose!")
    else:
        print("You win!")
elif user_choice == 2:
    if computer_choice == 1:
        print("You win!")
    else:
        print("You lose!")
elif user_choice == 3:
    if computer_choice == 1:
        print("You lose!")
    else:
        print("You win!")

            