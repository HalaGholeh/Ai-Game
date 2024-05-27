# Ai-Game
# Magnetic Cave Game

## Project Overview

Magnetic Cave is a 2-player adversary game played on an 8x8 chessboard where each player tries to build a bridge of 5 magnetic bricks. The bricks of one player are represented by `■` and the bricks of the other player by `□`. Players take turns placing bricks, starting with `■`. The game is won by the first player to align 5 consecutive bricks horizontally, vertically, or diagonally. If the board is full and no player has won, the game ends in a tie.

## Game Rules

1. **Board Setup**: The game is played on an 8x8 chessboard.
2. **Player Turns**: Players take turns placing their bricks (`■` or `□`), starting with `■`.
3. **Brick Placement**: A brick can only be placed on an empty cell if it is stacked directly on the left or right wall, or is stacked to the left or the right of another brick (of any color).
4. **Winning Condition**: The game is won by the first player to align 5 consecutive bricks in a row, column, or diagonal.
5. **Tie Condition**: If the board is full and no player has aligned 5 bricks, the game ends in a tie.

## Implementation Details

The game is implemented using a minimax algorithm with a heuristic of your choice. The program must decide on the next move within 3 seconds of real time. Optionally, you can implement an alpha-beta search to optimize the minimax algorithm.

### Play Modes

Your program should support the following play modes:
1. Manual entry for both `■` and `□` moves.
2. Manual entry for `■` moves and automatic moves for `□`.
3. Manual entry for `□` moves and automatic moves for `■`.

After each move, the program must display the new configuration of the board.
