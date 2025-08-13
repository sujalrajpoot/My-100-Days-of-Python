'''Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water.
Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win.'''

import random

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'snake' and computer == 'water') or (player == 'water' and computer == 'gun') or (player == 'gun' and computer == 'snake'):
        return "You win!"
    else:
        return "You lose!"

print("Welcome to Snake, Water, Gun game!")
def snake_water_gun():
    choices = ['snake', 'water', 'gun']
    player_choice = input("Enter your choice (snake, water, gun): ").lower()
    
    if player_choice not in choices:
        print("Invalid choice. Please choose from 'snake', 'water', or 'gun'.")
        return
    
    computer_choice = random.choice(['snake', 'water', 'gun'])
    print(f"Computer choose: {computer_choice}")

    result = determine_winner(player_choice, computer_choice)
    print(result)

while True:
    snake_water_gun()