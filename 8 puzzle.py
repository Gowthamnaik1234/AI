
import heapq
goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def manhattan_distance(state):
    return sum(abs(i//3 - goal_state.index(state[i])//3) + abs(i%3 - goal_state.index(state[i])%3) for i in range(9) if state[i] != 0)
def generate_successors(state):
    empty_space = state.index(0)
    empty_row, empty_col = divmod(empty_space, 3)
    for move in moves:
        new_row, new_col = empty_row + move[0], empty_col + move[1]

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = state[:]
            new_index = new_row * 3 + new_col
            new_state[empty_space], new_state[new_index] = new_state[new_index], new_state[empty_space]
            yield new_state
def solve_8_puzzle(initial_state):
    priority_queue = [(0 + manhattan_distance(initial_state), 0, initial_state)]
    visited_states = set()
    while priority_queue:
        _, cost, current_state = heapq.heappop(priority_queue)
        if current_state == goal_state:
            return cost
        if tuple(current_state) in visited_states:
            continue
        visited_states.add(tuple(current_state))
        for successor in generate_successors(current_state):
            heapq.heappush(priority_queue, (cost + 1 + manhattan_distance(successor), cost + 1, successor))
    return -1
initial_state = list(map(int, input("Enter the initial state of the 8-Puzzle (use space as a separator, e.g., '1 2 3 8 0 4 7 6 5'): ").split()))
if len(initial_state) != 9:
    print("Invalid input. Please provide 9 values.")
else:
    steps = solve_8_puzzle(initial_state)
    if steps != -1:
        print(f"Solution found in {steps} steps.")
    else:
        print("No solution found.")
