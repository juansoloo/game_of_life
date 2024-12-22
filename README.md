## Game of Life

This repository contains an implementation of Conway's Game of Life, written in Python using numpy. The Game of Life is a cellular automaton devised by mathematician John Conway, where a grid of cells evolves through iterations based on a set of simple rules.

## How It Works

The program generates an initial grid of cells, where each cell is either "alive" or "dead". The cells then evolve over time based on the following rules:

1. Any live cell with fewer than two live neighbors dies (underpopulation).

2. Any live cell with two or three live neighbors continues to live.

3. Any live cell with more than three live neighbors dies (overpopulation).

4. Any dead cell with exactly three live neighbors becomes a live cell (reproduction).

This implementation follows the tutorial by Robert Heaton.

 ## Features

- Randomized Initial State: The board can start with a random configuration of live and dead cells.

- Customizable Grid Size: You can specify the height and width of the board.

- Continuous Simulation: The simulation runs in a loop, updating and displaying the board in real-time.

- Optimized Implementation: Uses numpy for efficient array manipulations.
