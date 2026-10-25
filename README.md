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

### Project 1: Knowledge
- **[Knights](knights/)**: Solve Knights and Knaves logic puzzles using Propositional Logic and Model Checking.
  - Implementation: Knowledge bases `knowledge0`, `knowledge1`, `knowledge2`, and `knowledge3` in [`puzzle.py`](knights/puzzle.py)
  - Encodes general problem rules (knight or knave, not both) and character statements via logical biconditionals/implications.
- **[Minesweeper](minesweeper/)**: Knowledge-based AI agent to play Minesweeper using propositional logic sentences and subset-based inference.
  - Implementation: `Sentence` methods and `MinesweeperAI` methods (`add_knowledge`, `make_safe_move`, `make_random_move`) in [`minesweeper.py`](minesweeper/minesweeper.py)
  - Graphical interface playable via `runner.py`.

### Project 2: Uncertainty
- **[PageRank](pagerank/)**: Estimate web page importance using both a Markov Chain Random Surfer sampling model and the recursive iterative PageRank algorithm.
  - Implementation: `transition_model`, `sample_pagerank`, and `iterate_pagerank` in [`pagerank.py`](pagerank/pagerank.py)
- **[Heredity](heredity/)**: Assess the likelihood that a person carries mutated genes and exhibits genetic traits using a Bayesian Network.
  - Implementation: `joint_probability`, `update`, and `normalize` in [`heredity.py`](heredity/heredity.py)

### Project 3: Optimization
- **[Crossword](crossword/)**: Generate crossword puzzles modeled as a Constraint Satisfaction Problem (CSP).
  - Implementation: `enforce_node_consistency`, `revise`, `ac3`, `assignment_complete`, `consistent`, `order_domain_values`, `select_unassigned_variable`, and `backtrack` in [`generate.py`](crossword/generate.py)
  - Uses AC-3 for arc consistency, Minimum Remaining Values (MRV) & Degree Heuristic for variable selection, and Least-Constraining Values (LCV) for value ordering.

### Project 4: Learning
- **[Shopping](shopping/)**: Predict online customer purchase intent using a $k$-Nearest Neighbors classifier ($k=1$).
  - Implementation: `load_data`, `train_model`, and `evaluate` (sensitivity & specificity) in [`shopping.py`](shopping/shopping.py)
