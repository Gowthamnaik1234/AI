initial_state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
def print_board(board):
    for row in board:
        print(" ".join(["X" if cell == 1 else "O" if cell == -1 else " " for cell in row]))
def is_game_over(board):
    for row in board:
        if all(cell == 1 for cell in row) or all(cell == -1 for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == 1 for row in range(3)) or all(board[row][col] == -1 for row in range(3)):
            return True
    if all(board[i][i] == 1 for i in range(3)) or all(board[i][2 - i] == 1 for i in range(3)):
        return True
    if all(board[i][i] == -1 for i in range(3)) or all(board[i][2 - i] == -1 for i in range(3)):
        return True
    if all(cell != 0 for row in board for cell in row):
        return True
    return False
def evaluate(board):
    for row in board:
        if all(cell == 1 for cell in row):
            return 1
        if all(cell == -1 for cell in row):
            return -1
    for col in range(3):
        if all(board[row][col] == 1 for row in range(3)):
            return 1
        if all(board[row][col] == -1 for row in range(3)):
            return -1
    if all(board[i][i] == 1 for i in range(3)) or all(board[i][2 - i] == 1 for i in range(3)):
        return 1
    if all(board[i][i] == -1 for i in range(3)) or all(board[i][2 - i] == -1 for i in range(3)):
        return -1
    return 0
def minimax(board, depth, is_maximizing):
    if is_game_over(board):
        return evaluate(board)
    if is_maximizing:
        max_eval = float('-inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == 0:
                    board[row][col] = 1
                    eval = minimax(board, depth + 1, False)
                    board[row][col] = 0
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == 0:
                    board[row][col] = -1
                    eval = minimax(board, depth + 1, True)
                    board[row][col] = 0
                    min_eval = min(min_eval, eval)
        return min_eval
def find_best_move(board):
    best_eval = float('-inf')
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                board[row][col] = -1
                move_eval = minimax(board, 0, True)
                board[row][col] = 0
                if move_eval > best_eval:
                    best_eval = move_eval
                    best_move = (row, col)
    return best_move
while not is_game_over(initial_state):
    print_board(initial_state)
    player_move = input("Enter your move (row and column, e.g., 0 1): ")
    player_row, player_col = map(int, player_move.split())
    if initial_state[player_row][player_col] == 0:
        initial_state[player_row][player_col] = 1
    else:
        print("Invalid move. Try again.")
        continue

    if is_game_over(initial_state):
        break
    computer_move = find_best_move(initial_state)
    if computer_move is not None:
        computer_row, computer_col = computer_move
        initial_state[computer_row][computer_col] = -1
    else:
        print("It's a draw!")
        break
print_board(initial_state)
result = evaluate(initial_state)
if result == 1:
    print("You win!")
elif result == -1:
    print("Computer wins!")
else:
    print("It's a draw!")
