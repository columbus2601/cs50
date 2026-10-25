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
- **[Nim](nim/)**: Reinforcement learning agent that learns to play Nim optimally via Q-learning and $\epsilon$-greedy exploration.
  - Implementation: `get_q_value`, `update_q_value`, `best_future_reward`, and `choose_action` in [`nim.py`](nim/nim.py)

### Project 5: Neural Networks
- **[Traffic](traffic/)**: Convolutional Neural Network (CNN) in TensorFlow/Keras to classify 43 categories of road signs from the German Traffic Sign Recognition Benchmark (GTSRB).
  - Implementation: `load_data` and `get_model` in [`traffic.py`](traffic/traffic.py)
  - Experimentation writeup: [`README.md`](traffic/README.md)
  - Achieves $98.57\%$ test accuracy on over 10,000 test images.

### Project 6: Language
- **[Parser](parser/)**: Context-Free Grammar (CFG) parser in Python with NLTK to parse sentences and extract Noun Phrase (NP) chunks.
  - Implementation: `preprocess`, `np_chunk`, and `NONTERMINALS` CFG production rules in [`parser.py`](parser/parser.py)
  - Parses compound sentences, multi-adjective phrases, adverbials, prepositional attachments, and identifies non-nested noun phrase chunks.
- **[Attention](attention/)**: Transformer-based Masked Language Model using BERT (`bert-base-uncased`) to predict masked tokens and visualize attention maps across 144 attention heads.
  - Implementation: `get_mask_token_index`, `get_color_for_attention_score`, and `visualize_attentions` in [`mask.py`](attention/mask.py)
  - Attention analysis writeup: [`analysis.md`](attention/analysis.md) (identifying previous-token tracking in Layer 4 Head 6 and modifier-to-noun binding in Layer 5 Head 6).
