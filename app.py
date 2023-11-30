import os
import random

choices = ['rock', 'paper', 'scissors']
score = 0

os.system('cls')

while True:
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input('rock, paper or scissors? ').lower()

    if player == computer:
        print("It's a tie!")
    elif (player == 'rock' and computer == 'scissors') or (player == 'paper' and computer == 'rock') or (player == 'scissors' and computer == 'paper'):
        print("You win!")
        score += 1
    else:
        print("Computer wins!")

    print(f"Player: {player} vs Computer: {computer}")
    print(f"Score: {score}")

    play_again = input("Do you want to play again? (yes/no) ").lower()
    if play_again != "yes":
        break
    print(f"Score: {score}")


     