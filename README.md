## Tetris-Style Polyomino Puzzle Solver
This project is a Python-based solver for tiling puzzles using Tetris-like pieces (polyominoes). The goal is to fill a custom-shaped board completely using all given pieces, without overlaps or gaps — even when the board contains holes.

🔍 How It Works
- Uses a backtracking algorithm to try all possible piece placements.
- Each piece can be rotated and flipped.
- The board is defined as a 2D grid, where 1 = valid cell and 0 = empty/hole.
- If a solution is found, the final board is visualized with matplotlib, using colored tiles for each piece.

🧠 Highlights
- Supports custom boards with irregular shapes and voids.
- Easy to define and modify pieces.
- Based on polyomino tiling and exact cover principles.
- Useful for puzzle games, logic challenges, or educational tools.

▶️ Requirements
- Python 3
