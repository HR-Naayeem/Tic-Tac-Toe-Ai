import random
from tictactoe_ai import minimax, check_winner

def random_move(board):
    moves = [i for i in range(9) if board[i] == " "]
    return random.choice(moves)

def play_game_full():
    """AI uses full-depth minimax with alpha-beta (no heuristic)."""
    board = [" "] * 9
    current = "X"  # AI is X

    while True:
        if current == "X":  # AI plays X
            _, move = minimax(board, player="X", use_heuristic=False)  # no heuristic, full search
            board[move] = "X"
        else:               # Random plays O
            m = random_move(board)
            board[m] = "O"

        winner = check_winner(board)
        if winner:
            return winner
        
        current = "O" if current == "X" else "X"


def play_game_cutoff(cutoff):
    """AI uses minimax + alpha-beta + heuristic with depth cutoff."""
    board = [" "] * 9
    current = "X"

    while True:
        if current == "X":  # AI plays X
            _, move = minimax(board, player="X", use_heuristic=True, cutoff=cutoff)
            board[move] = "X"
        else:               # Random plays O
            m = random_move(board)
            board[m] = "O"

        winner = check_winner(board)
        if winner:
            return winner
        
        current = "O" if current == "X" else "X"


def simulate_full(games=50):
    results = {"X":0, "O":0, "Draw":0}
    for _ in range(games):
        result = play_game_full()
        results[result] += 1
    return results

def simulate_cutoff(cutoff, games=50):
    results = {"X":0, "O":0, "Draw":0}
    for _ in range(games):
        result = play_game_cutoff(cutoff)
        results[result] += 1
    return results


if __name__ == "__main__":
    G = 50  # number of games for each setting

    full = simulate_full(G)
    print("Full-depth (no heuristic):", full)

    c4 = simulate_cutoff(4, G)
    print("Cutoff 4 + heuristic:", c4)

    c2 = simulate_cutoff(2, G)
    print("Cutoff 2 + heuristic:", c2)
