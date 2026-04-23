import time
import tictactoe_ai as ai  # use module alias instead of importing variables


def print_board(board):
    """Print the Tic Tac Toe board."""
    for i in range(3):
        print(" | ".join(board[i * 3:(i + 1) * 3]))
        if i < 2:
            print("---------")


def player_move(board, human_player):
    """Handle player's move input."""
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit():
            move = int(move) - 1
            if 0 <= move < 9 and board[move] == " ":
                board[move] = human_player
                break
            else:
                print("Invalid move! Cell occupied or out of range.")
        else:
            print("Invalid input. Please enter a number (1–9).")


def ai_move(board, ai_player, use_heuristic=True, cutoff=6, show_stats=False):
    """
    Make the AI choose the best move using minimax.

    Parameters
    ----------
    board : list
        Current board state.
    ai_player : str
        'X' or 'O' for the AI.
    use_heuristic : bool
        Whether to use heuristic evaluation with depth cutoff.
    cutoff : int or None
        Maximum search depth; if None, search full depth.
    show_stats : bool
        If True, prints nodes explored and time taken (for experiments).
    """
    print("AI is thinking...")

    # reset counter in tictactoe_ai module
    ai.nodes_explored = 0

    start_time = time.perf_counter()
    score, move = ai.minimax(
        board,
        player=ai_player,
        use_heuristic=use_heuristic,
        cutoff=cutoff
    )
    end_time = time.perf_counter()

    if move is not None:
        board[move] = ai_player
    else:
        print("No valid moves left.")

    if show_stats:
        elapsed_ms = (end_time - start_time) * 1000
        print(f"AI score: {score}")
        print(f"Nodes explored: {ai.nodes_explored}")
        print(f"Time per move: {elapsed_ms:.2f} ms")
