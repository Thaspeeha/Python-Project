# Function to display the current game board
def print_board(board):
    """Displays the current state of the 3x3 board."""
    print("\nCurrent board:")
    for row in board:
        # Join each cell in the row with a separator and print
        print(" | ".join(row))
        # Print a line separator between rows
        print("-" * 9)

# Function to check if a player has won the game
def check_winner(board, player):
    """Checks whether the current player has a winning combination."""
    # Check all rows for a win
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
    # Check all columns for a win
    for i in range(3):
        if all(board[j][i] == player for j in range(3)):
            return True
    # Check main diagonal
    if all(board[i][i] == player for i in range(3)):
        return True
    # Check anti-diagonal
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    # No winning combination found
    return False

# Function to check if the game ended in a draw
def is_draw(board):
    """Returns True if all cells are filled and there's no winner."""
    # A draw happens when every cell is filled with 'X' or 'O'
    return all(cell in ["X", "O"] for row in board for cell in row)

# Function to get and validate the current player's move
def get_move(player, board):
    """
    Prompts the current player to enter a move (row and column),
    validates the move, and returns the position as (row, col).
    """
    while True:
        try:
            # Ask player for input
            move = input(f"Player {player}, enter your move as row and column (e.g. 1 2): ")
            # Convert input to two integers (row and column)
            row, col = map(int, move.split())
            # Validate row and column range
            if row in [1, 2, 3] and col in [1, 2, 3]:
                # Check if the chosen cell is not already taken
                if board[row - 1][col - 1] not in ["X", "O"]:
                    return row - 1, col - 1  # Adjust index to start from 0
                else:
                    print("That spot is already taken. Try again.")
            else:
                print("Invalid input. Row and column must be between 1 and 3.")
        except ValueError:
            # Handle non-integer or wrong format input
            print("Invalid input. Please enter two numbers separated by a space.")

# Main function to play the Tic Tac Toe game
def play_game():
    """Runs the main game loop for Tic Tac Toe."""
    print("Welcome to Tic Tac Toe!\n")
    
    while True:
        # Create a blank 3x3 board
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "X"  # X always starts first
        game_over = False     # Flag to track game status

        # Play rounds until game ends (win or draw)
        while not game_over:
            print_board(board)                      # Show the board
            row, col = get_move(current_player, board)  # Get valid move
            board[row][col] = current_player        # Mark the cell with player's symbol

            # Check if current player has won
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!\n")
                game_over = True
            # Check for a draw
            elif is_draw(board):
                print_board(board)
                print("It's a draw!\n")
                game_over = True
            else:
                # Switch to the other player
                current_player = "O" if current_player == "X" else "X"

        # Ask if players want to play another game
        replay = input("Do you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("Thanks for playing Tic Tac Toe!")
            break  # Exit the game loop

# Entry point: start the game
if __name__ == "__main__":
    play_game()
