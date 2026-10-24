"""
================================================================================
ARTIFICIAL INTELLIGENCE: N-QUEENS PROBLEM
================================================================================

ALGORITHM (Backtracking Approach):
----------------------------------
1. Start in the leftmost column (Column 0).
2. If all queens are successfully placed (Column == N), a solution is found. Return True.
3. Try placing a queen in all rows of the current column one by one.
4. For each row, check if placing the queen is safe using the 'is_safe' function:
   - Check the horizontal row to the left.
   - Check the upper diagonal to the left.
   - Check the lower diagonal to the left.
   (No need to check the right side because we place queens column by column from left to right).
5. If the placement is SAFE:
   - Mark this [Row, Column] position on the board with a 1 (Queen placed).
   - Recursively repeat the process for the next column: solve_n_queens_util(board, col + 1).
   - If moving forward leads to a successful solution, return True.
   - If moving forward leads to a dead-end (no safe spaces in future columns), BACKTRACK:
     Remove the queen (change 1 back to 0) and try the next row in the current column.
6. If all rows in the current column have been tried and none work, return False to trigger
   backtracking in the previous column.
================================================================================
"""

import sys

def print_board(board, N):
    """Helper function to print the chess board cleanly to the console."""
    print(f"\n--- Solution for {N}-Queens ---")
    for row in board:
        # Replaces 1 with 'Q' and 0 with '.' for visual clarity
        line = " ".join("Q" if cell == 1 else "." for cell in row)
        print(line)
    print("-" * (N * 2 + 15))


def is_safe(board, row, col, N):
    """
    Checks if a queen can be safely placed at board[row][col].
    We only check the left side because queens are placed column by column from left to right.
    """
    # 1. Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # 2. Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # 3. Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, col, N):
    """Base backtracking utility function to solve the N-Queens problem."""
    # Base Case: If all queens are placed, return True
    if col >= N:
        return True

    # Consider this column and try placing a queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place the queen
            board[i][col] = 1

            # Recur to place the rest of the queens
            if solve_n_queens_util(board, col + 1, N):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then BACKTRACK by removing the queen from board[i][col]
            board[i][col] = 0

    # If the queen cannot be placed in any row of this column, return False
    return False


def main():
    print("--- Artificial Intelligence: N-Queens Solver ---")
    
    # 1. RUNTIME INPUT & ERROR HANDLING
    try:
        n_input = input("Enter the number of Queens (N): ").strip()
        N = int(n_input)
    except ValueError:
        print("Error: Input must be a valid whole number.")
        sys.exit()

    # Enforce constraints: No more than 8 queens, and must be at least 1
    if N > 8:
        print(f"Error: The maximum allowed number of queens is 8. You entered {N}.")
        print("Processing states larger than 8 requires advanced optimization beyond basic backtracking.")
        sys.exit()
    elif N < 1:
        print("Error: The number of queens must be 1 or greater.")
        sys.exit()
        
    # Handle mathematical impossible layout notifications
    if N in (2, 3):
        print(f"\nNote: Mathematically, a solution does not exist for a {N}x{N} board.")
        print("The program will attempt execution but expect a failure message.")

    # 2. INITIALIZE BOARD
    # Create an NxN matrix filled with 0s
    board = [[0 for _ in range(N)] for _ in range(N)]

    # 3. SOLVE THE PROBLEM
    if not solve_n_queens_util(board, 0, N):
        print(f"\n[Result] No valid solution exists for {N} Queens.")
    else:
        # 4. OUTPUT THE RESULT
        print_board(board, N)


if __name__ == "__main__":
    main()
