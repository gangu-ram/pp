import math

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_winner(board, player):
    for row in board + list(zip(*board)):  # Check rows and columns
        if all(cell == player for cell in row):
            return True

    diagonals = [board[i][i] for i in range(3)], [board[i][2 - i] for i in range(3)]
    if any(all(cell == player for cell in diag) for diag in diagonals):  # Check diagonals
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def evaluate(board):
    for player in ['X', 'O']:
        if is_winner(board, player):
            return 1 if player == 'X' else -1

    return 0 if is_board_full(board) else None

def minimax(board, is_maximizing_player, alpha, beta):
    score = evaluate(board)

    if score is not None:
        return score

    best_val = -math.inf if is_maximizing_player else math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X' if is_maximizing_player else 'O'
                eval_score = minimax(board, not is_maximizing_player, alpha, beta)
                board[i][j] = ' '

                best_val = max(best_val, eval_score) if is_maximizing_player else min(best_val, eval_score)
                alpha = max(alpha, eval_score) if is_maximizing_player else alpha
                beta = min(beta, eval_score) if not is_maximizing_player else beta

                if beta <= alpha:
                    break

    return best_val

def find_best_move(board):
    best_val, best_move = -math.inf, (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, False, -math.inf, math.inf)
                board[i][j] = ' '

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]

    print("Tic-Tac-Toe with Alpha-Beta Pruning")
    print_board(board)

    while True:
        try:
            player_row, player_col = map(int, input("Enter row and column (0, 1, 2) separated by space: ").split())
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")
            continue

        if not (0 <= player_row < 3 and 0 <= player_col < 3):
            print("Invalid input. Row and column must be in the range 0 to 2.")
            continue

        if board[player_row][player_col] != ' ':
            print("Cell already occupied. Try again.")
            continue

        board[player_row][player_col] = 'O'
        print_board(board)

        if is_winner(board, 'O'):
            print("You win!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

        print("Computer's turn:")
        computer_row, computer_col = find_best_move(board)
        board[computer_row][computer_col] = 'X'
        print_board(board)

        if is_winner(board, 'X'):
            print("Computer wins!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
