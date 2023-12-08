import math

def print_board(board):
    [print(" ".join(row)) for row in board]
    print()

def is_winner(board, player):
    return any(all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)) for i in range(3)) or \
           any(all(board[i][i] == player for i in range(3)), all(board[i][2 - i] == player for i in range(3)))

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def evaluate(board):
    for player in ['X', 'O']:
        if is_winner(board, player):
            return 1 if player == 'X' else -1
    return 0 if is_board_full(board) else None

def minimax(board, depth, maximizing_player, alpha, beta):
    score = evaluate(board)

    if score is not None:
        return score

    val = -math.inf if maximizing_player else math.inf

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j], val = 'X' if maximizing_player else 'O', \
                                  max(val, minimax(board, depth + 1, not maximizing_player, alpha, beta) if maximizing_player else
                                      minimax(board, depth + 1, not maximizing_player, alpha, beta))
                board[i][j] = ' '
                alpha, beta = max(alpha, val) if maximizing_player else alpha, min(beta, val) if not maximizing_player else beta
                if beta <= alpha:
                    break

    return val

def find_best_move(board):
    return max(((i, j) for i in range(3) for j in range(3) if board[i][j] == ' '),
               key=lambda move: minimax([[cell for cell in row] for row in board], 0, False, -math.inf, math.inf))

def play_tic_tac_toe():
    board, current_player = [[' ']*3 for _ in range(3)], 'X'

    while True:
        print_board(board)
        if current_player == 'X':
            row, col = find_best_move(board)
            print(f"Computer (X) plays at row {row + 1}, column {col + 1}")
        else:
            row, col = [int(input(f"Enter {coord} (1, 2, or 3): ")) - 1 for coord in ('row', 'column')]

        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("Cell already occupied. Try again.")
            continue

        winner = evaluate(board)
        if winner is not None:
            print_board(board)
            print(f"{'Computer (X)' if winner == 1 else 'Player (O)'} wins!" if winner != 0 else "It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_tic_tac_toe()
