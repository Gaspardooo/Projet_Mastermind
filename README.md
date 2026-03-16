# Mastermind: Combinatorial Optimization & Adaptive Algorithms

This project is a high-level implementation of the Mastermind game, focusing on **deterministic optimization** and **state-space search**. It demonstrates the transition from brute-force approaches to optimal decision-making under constraints.

## Technical Core

### 1. Optimization Strategies (Codebreaker)
The project implements several layers of algorithmic complexity for the Codebreaker:
- **Heuristic Filtering:** A strategy that dynamically updates the set of possible solutions based on previous evaluations, drastically reducing the search space at each turn.
- **Minimax Optimization (Knuth's Algorithm):** An optimal strategy that evaluates every possible guess (even those no longer possible) to minimize the maximum number of remaining potential solutions in the worst-case scenario.

### 2. Adaptive System (Codemaker)
- **Non-Deterministic Resistance:** The advanced Codemaker does not rely on a fixed secret code. It utilizes a "cheating" logic that maintains a pool of all valid solutions and dynamically adapts to the Codebreaker's guesses to maximize the game length.
- **Integrity Validation:** A log-analysis tool (`check_codemaker.py`) was developed to verify the mathematical consistency of the Codemaker's hints against the final revealed solution.

### 3. Graphical Interface
- Built with **Tkinter**, the GUI provides a fully interactive experience, linking the underlying algorithmic engine to a visual board.
- Features include real-time evaluation display and dynamic turn management.

## Algorithmic Analysis
The project includes a technical report covering:
- **Statistical Validation:** Comparison of empirical results with analytical expectations.
- **Complexity Study:** Measuring the impact of Minimax optimization against adaptive adversaries.

## Tech Stack
- **Language:** Python 3
- **Libraries:** Tkinter (GUI), Matplotlib (Analysis), NumPy.
