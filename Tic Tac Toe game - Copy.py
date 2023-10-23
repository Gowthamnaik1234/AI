def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        
        try:
            while True:
                row, col = map(int, input(f"Player {current_player}, enter row (0-2) and column (0-2) separated by space: ").split())
                if row not in [0, 1, 2] or col not in [0, 1, 2]:
                    print("Invalid input. Please enter numbers between 0 and 2.")
                    continue
                if board[row][col] == " ":
                    break
                else:
                    print("That cell is already taken. Try again.")
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    play_tic_tac_toe()
