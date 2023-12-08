def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_queens(board, row):
    n = len(board)
    if row == n:
        # All queens are placed successfully
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            # Place queen and move to the next row
            board[row] = col
            solve_queens(board, row + 1)
            # Backtrack if placing the queen in the current position doesn't lead to a solution
            board[row] = -1

def print_solution(board):
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

def four_queens():
    # Initialize the board with -1, indicating no queen is placed initially
    board = [-1] * 4
    solve_queens(board, 0)

if __name__ == "__main__":
    four_queens()
