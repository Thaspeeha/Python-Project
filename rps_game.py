import random

# Function to get the user's choice and validate the input
def get_player_choice():
    while True:
        choice = input("Enter your choice (rock, paper, scissors or quit to exit): ").lower()
        if choice in ["rock", "paper", "scissors", "quit"]:
            return choice
        else:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")

# Function to randomly choose the computer's move
def get_com_playerchoice():
    return random.choice(["rock", "paper", "scissors"])

# Function to determine the winner of the round
def determine_winner(user, computer):
    if user == computer:
        return "draw"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

# Function to display the result of the round
def display_result(user, computer, winner):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")
    if winner == "draw":
        print("It's a draw!")
    elif winner == "user":
        print("You win this round!")
    else:
        print("Computer wins this round!")

# Main function to control the game flow
def play_game():
    print("Welcome to Rock, Paper, Scissors!")  # Welcome message
    user_score = 0         # Track user score
    computer_score = 0     # Track computer score
    round_number = 1       # Track the number of rounds

    while True:
        print(f"\n--- Round {round_number} ---")
        user_choice = get_player_choice()  # Get user input
        if user_choice == "quit":        # Exit game if user types 'quit'
            break

        computer_choice = get_com_playerchoice()     # Computer makes a choice
        winner = determine_winner(user_choice, computer_choice)  # Determine winner
        display_result(user_choice, computer_choice, winner)     # Display round result

        # Update scores based on winner
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        # Display current score
        print(f"\nScore => You: {user_score}, Computer: {computer_score}")
        round_number += 1  # Go to next round

    # Game over - display final results
    print("\nThanks for playing!")
    print(f"Final Score => You: {user_score}, Computer: {computer_score}")
    if user_score > computer_score:
        print("Congratulations, you won the game!")
    elif computer_score > user_score:
        print("Computer wins the game! Better luck next time.")
    else:
        print("The game ended in a draw!")

# Entry point of the script
if __name__ == "__main__":
    play_game()
