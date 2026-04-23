from tictactoe_game import print_board, ai_move, player_move
from tictactoe_ai import check_winner

def play_game(human_player, ai_player, cutoff):
    """Play a single game of Tic Tac Toe."""
    board = [" "] * 9
    current_player = "X"  # X always starts
    use_heuristic = True

    while True:
        print_board(board)

        result = check_winner(board)
        if result:
            if result == "Draw":
                print("It's a draw!")
            else:
                print(f"{result} wins!")
            break

        if current_player == human_player:
            player_move(board, human_player)
        else:
            ai_move(board, ai_player, use_heuristic, cutoff, show_stats=True)

        current_player = "O" if current_player == "X" else "X"
        print()

def main():
    """Main function to run the Tic Tac Toe game."""
    human_player = ""
    ai_player = ""

    # Player chooses symbol
    while human_player not in ["X", "O"]:
        human_player = input("Choose your side (X/O): ").upper()

    ai_player = "O" if human_player == "X" else "X"

    # Display board positions for reference
    print("\nBoard positions:")
    print(" 1 | 2 | 3")
    print("-----------")
    print(" 4 | 5 | 6")
    print("-----------")
    print(" 7 | 8 | 9\n")

    # Ask if heuristic should be used
    use_heuristic = True

    # Difficulty selection
    print("\nSelect AI Difficulty Level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    difficulty = input("Enter 1, 2, or 3: ")

    if difficulty == "1":
        cutoff = 2
    elif difficulty == "2":
        cutoff = 4
    else:
        cutoff = 6  # Hard level (deeper Minimax search)

    # Game loop
    while True:
        print("\nGame start!\n")
        play_game(human_player, ai_player, cutoff)
        
        play_again = input("\nPlay Again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing!")
            break
        print("\n" + "="*20 + "\n")

if __name__ == "__main__":
    main()
