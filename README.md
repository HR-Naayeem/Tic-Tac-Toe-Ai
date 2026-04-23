# Tic-Tac-Toe AI – Minimax with Alpha-Beta Pruning

![PYTHON](https://img.shields.io/badge/PYTHON-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MINIMAX](https://img.shields.io/badge/MINIMAX-0A192F?style=for-the-badge)
![ALPHA--BETA PRUNING](https://img.shields.io/badge/ALPHA--BETA%20PRUNING-6D28D9?style=for-the-badge)
![HEURISTIC EVALUATION](https://img.shields.io/badge/HEURISTIC%20EVALUATION-EA580C?style=for-the-badge)
![CLI GAME](https://img.shields.io/badge/CLI%20GAME-16A34A?style=for-the-badge)

---

Python-based Tic-Tac-Toe game featuring an AI opponent that uses Minimax, Alpha-Beta pruning, and heuristic evaluation to make decisions across multiple difficulty levels.

## Overview

This project was developed as part of an Artificial Intelligence course to demonstrate game tree search, adversarial decision-making, pruning for efficiency, and difficulty control through search depth. The game runs in the command line and allows a human player to compete against an AI on a standard 3×3 board.

## Key Features

- Human vs AI Tic-Tac-Toe on a 3×3 board
- AI opponent powered by the Minimax algorithm
- Alpha-Beta pruning for faster decision-making
- Heuristic evaluation for non-terminal board states
- Easy, Medium, and Hard difficulty levels
- Adjustable search depth for difficulty control
- Command-line gameplay with no external libraries required

## Tech Stack

### Language
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

### AI Concepts / Algorithms
![Minimax](https://img.shields.io/badge/Minimax-0A192F?style=for-the-badge)
![Alpha-Beta Pruning](https://img.shields.io/badge/Alpha--Beta%20Pruning-6D28D9?style=for-the-badge)
![Heuristic Evaluation](https://img.shields.io/badge/Heuristic%20Evaluation-EA580C?style=for-the-badge)
![Game Tree Search](https://img.shields.io/badge/Game%20Tree%20Search-2563EB?style=for-the-badge)

### Interface
![Command Line](https://img.shields.io/badge/Command%20Line-16A34A?style=for-the-badge)

## Architecture

```text
Player Input
   ↓
Game Loop (main.py)
   ↓
Board State Management
   ↓
AI Evaluation (Minimax + Alpha-Beta + Heuristic)
   ↓
Best Move Selection
   ↓
Board Update / Winner Check
```

## How It Works

1. The player starts the game and chooses a symbol and difficulty level.
2. The game board is maintained as a list of 9 cells representing the 3×3 grid.
3. On the AI’s turn, the program generates legal moves and evaluates future board states.
4. Minimax explores possible outcomes by maximizing the AI’s score and minimizing the opponent’s score.
5. Alpha-Beta pruning removes branches that cannot affect the final decision, improving efficiency.
6. For limited-depth difficulties, the AI stops early and uses a heuristic function to estimate board strength.
7. The game continues until there is a win, loss, or draw.

## Difficulty Levels

- **Easy** — shallow search depth, more mistakes, easier to beat
- **Medium** — deeper search with stronger move selection
- **Hard** — deep or near-complete search, close to optimal play

## Challenges Solved

- Implemented adversarial search for turn-based decision-making
- Improved search performance using Alpha-Beta pruning
- Added heuristic evaluation for limited-depth gameplay
- Balanced difficulty by controlling cutoff depth
- Structured the project into separate modules for game logic, AI logic, and simulation

## Project Structure

```text
tic-tac-toe-ai/
├── README.md
├── .gitignore
├── main.py
├── simulate.py
├── tictactoe_ai.py
├── tictactoe_game.py
└── report/
    └── Project Report.pdf
```

## File Details

- `main.py` — main entry point, game flow, user choices, and repeated gameplay
- `simulate.py` — simulation or testing logic for evaluating gameplay behavior
- `tictactoe_ai.py` — AI logic including Minimax, Alpha-Beta pruning, heuristic evaluation, and move ordering
- `tictactoe_game.py` — board display, player moves, AI move integration, and game state handling
- `project-report/` — report and supporting documentation for the project

## How to Run

### Requirements
- Python 3.x
- No external libraries required

### Steps

```bash
git clone https://github.com/HR-Naayeem/tic-tac-toe-ai.git
cd tic-tac-toe-ai
python main.py
```

## Future Improvements

- Add a graphical user interface
- Add score tracking across multiple rounds
- Improve the heuristic evaluation function
- Add AI vs AI mode
- Include performance statistics such as search depth and explored nodes

## Notes

This project focuses on core Artificial Intelligence concepts such as Minimax search, Alpha-Beta pruning, and heuristic-based evaluation. It was designed as a lightweight command-line project without external dependencies, making it easy to run and study.