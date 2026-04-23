# tictactoe_ai.py
# Heurestic logic 
# Authors: Md Hasibur Rahman and Sanjida AKhter


import math
nodes_explored = 0

def check_winner(board):
    lines = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for a,b,c in lines:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    if " " not in board:
        return "Draw"
    return None


def heuristic(board, player):
    opponent = 'O' if player == 'X' else 'X'
    lines = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    score = 0
    for line in lines:
        vals = [board[i] for i in line]
        # AI patterns
        if vals.count(player) == 2 and vals.count(" ") == 1: score += 10
        elif vals.count(player) == 1 and vals.count(" ") == 2: score += 1
        # Opponent threats
        if vals.count(opponent) == 2 and vals.count(" ") == 1: score -= 8
    return score

def legal_moves(board):
    return [i for i,c in enumerate(board) if c == " "]

def ordered_moves(board):
    # Improves pruning: center -> corners -> edges
    order = [4, 0, 2, 6, 8, 1, 3, 5, 7]
    return [i for i in order if board[i] == " "]

def minimax(board, depth=0, alpha=-math.inf, beta=math.inf,
            maximizing=True, player='X', use_heuristic=False, cutoff=4):
    """
    Minimax with alpha-beta. Scores are always from `player` (AI) perspective.
    If `use_heuristic` is True, apply a depth cutoff and return heuristic at cutoff.
    """
    global nodes_explored
    nodes_explored += 1

    winner = check_winner(board)
    if winner:
        if winner == player:           # AI wins
            return 10 - depth, None
        elif winner == "Draw":
            return 0, None
        else:                           # Opponent wins
            return depth - 10, None

    # Depth cutoff for heuristic evaluation (for non-terminal states only)
    if use_heuristic and depth >= cutoff:
        return heuristic(board, player), None

    opponent = 'O' if player == 'X' else 'X'
    best_move = None

    if maximizing:
        best_score = -math.inf
        for i in ordered_moves(board):
            board[i] = player
            score, _ = minimax(board, depth+1, alpha, beta, False, player, use_heuristic, cutoff)
            board[i] = " "
            if score > best_score:
                best_score, best_move = score, i
            alpha = max(alpha, best_score)
            if beta <= alpha:  # prune
                break
        return best_score, best_move
    else:
        best_score = math.inf
        for i in ordered_moves(board):
            board[i] = opponent
            score, _ = minimax(board, depth+1, alpha, beta, True, player, use_heuristic, cutoff)
            board[i] = " "
            # ❗ Do NOT negate score; evaluation is already from AI perspective
            if score < best_score:
                best_score, best_move = score, i
            beta = min(beta, best_score)
            if beta <= alpha:  # prune
                break
        return best_score, best_move
