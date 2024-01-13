"""Let's build an interactive console game of rock, paper, scissors!

The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
By the end of each round, the player can choose whether to play again.
Display the player's score at the end of the game.
The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.
"""

import random

# Define the options
options = ["rock", "paper", "scissors"]

# Define a function that returns the winner of each round
def winner(player, computer):
    # If the player and computer chose the same option, return "tie"
    # If the player chose rock and the computer chose scissors, return "player"
    # If the player chose paper and the computer chose rock, return "player"
    # If the player chose scissors and the computer chose paper, return "player"
    # If the player chose scissors and the computer chose rock, return "computer"
    # If the player chose rock and the computer chose paper, return "computer"
    # If the player chose paper and the computer chose scissors, return "computer"
    # If the player chose an invalid option, return "invalid"
    if player == computer:
        return "tie"
    elif player == "rock" and computer == "scissors":
        return "player"
    elif player == "paper" and computer == "rock":
        return "player"
    elif player == "scissors" and computer == "paper":
        return "player"
    elif player == "scissors" and computer == "rock":
        return "computer"
    elif player == "rock" and computer == "paper":
        return "computer"
    elif player == "paper" and computer == "scissors":
        return "computer"
    else:
        return "invalid"    
    
# Define a function that checks if the player wants to play again
def play_again():
    # Ask the player if they want to play again
    # If the player wants to play again, return True
    # If the player doesn't want to play again, return False
    # If the player enters an invalid option, ask them again
    print("Do you want to play again? (y/n)")
    answer = input()
    if answer == "y":
        return True
    elif answer == "n":
        return False
    else:
        print("Invalid option. Try again.")
        play_again()
    return

# Define the main function that runs the game
def main():
    print("Welcome to Rock, Paper, Scissors!")
    # Define the score
    # Define the player's choice
    # Define the computer's choice
    # Define the winner of the round
    # Define the play again option
    score = 0
    player_choice = ""
    computer_choice = ""
    round_winner = ""
    play_again_option = True

    # While the player wants to play again, run the game
    while play_again_option == True:
        # Ask the player for their choice
        print("Choose rock, paper, or scissors.")
        player_choice = input().lower()
        # If the player's choice is valid, make the computer's choice
        if player_choice in options:
            computer_choice = random.choice(options)
            # Print the computer's choice
            print("The computer chose " + computer_choice + ".")
            # Determine the winner of the round
            round_winner = winner(player_choice, computer_choice)
            # If the player won the round, add 1 to the score
            if round_winner == "player":
                score += 1
                print("You won!")
            # If the computer won the round, subtract 1 from the score
            elif round_winner == "computer":
                score -= 1
                print("You lost!")
            # If the round was a tie, do not change the score
            elif round_winner == "tie":
                print("It's a tie!")
            # If the player entered an invalid option, do not change the score
            elif round_winner == "invalid":
                print("Invalid option. Try again.")
            # Print the score
            print("Your score is " + str(score) + ".")
        # If the player's choice is invalid, do not change the score
        else:
            print("Invalid option. Try again.")
        # Ask the player if they want to play again
        play_again_option = play_again()
    # Print the final score
    print("Your final score is " + str(score) + ".")
    # Print a goodbye message
    print("Thanks for playing!")
    # Exit the program
    exit()

# If this is the main file being executed, call main()
if __name__ == "__main__":
    main()