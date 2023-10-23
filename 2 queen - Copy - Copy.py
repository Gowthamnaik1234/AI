def is_safe(board):
    return board[0] != board[1] and abs(board[0] - board[1]) != 1
def solve_queen_problem():
    for queen1 in range(2):
        for queen2 in range(2):
            board = [queen1, queen2]
            if is_safe(board):
                return board
    return None
solution = solve_queen_problem()
if solution:
    print("Solution found:")
    for row, col in enumerate(solution):
        print(f"Queen {row + 1} at ({row + 1}, {col + 1})")
else:
    print("No solution exists.")
