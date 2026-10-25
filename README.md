# CS50 AI Solutions

Repository with solutions and tests for Harvard's CS50 AI (Introduction to Artificial Intelligence with Python).

## Projects

### Project 0: Search
- **[Degrees](degrees/)**: Find the shortest path (degrees of separation) between two actors using Breadth-First Search (BFS).
  - Implementation: `shortest_path(source, target)` in [`degrees.py`](degrees/degrees.py)
  - Uses Queue-based Breadth-First Search (BFS) with early goal checking and $O(1)$ state lookups.
- **[Tic-Tac-Toe](tictactoe/)**: Optimal Tic-Tac-Toe AI player using Minimax with Alpha-Beta Pruning.
  - Implementation: `player`, `actions`, `result`, `winner`, `terminal`, `utility`, and `minimax` in [`tictactoe.py`](tictactoe/tictactoe.py)
  - Includes graphical UI with `runner.py` (Pygame).
