from collections import deque

def is_safe(state):
    left_bank = state[0]
    right_bank = state[1]

    if (left_bank[0] < left_bank[1] or right_bank[0] < right_bank[1]) and left_bank != (0, 0):
        return False

    return True

def is_goal(state):
    return state == ((0, 0), (3, 3))

def get_next_states(state):
    next_states = []

    for i in range(3):
        for j in range(3):
            if i + j > 2 or i + j == 0:
                continue
            for direction in [1, -1]:
                delta = (i * direction, j * direction)
                new_state = ((state[0][0] - delta[0], state[0][1] - delta[1]),
                             (state[1][0] + delta[0], state[1][1] + delta[1]))
                if is_safe(new_state):
                    next_states.append(new_state)

    return next_states

def solve():
    initial_state = ((3, 3), (0, 0))
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        current_state, path = queue.popleft()

        if is_goal(current_state):
            return path

        visited.add(current_state)

        for next_state in get_next_states(current_state):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))

    return None

def print_solution(solution):
    if solution is None:
        print("No solution found.")
    else:
        for i, state in enumerate(solution):
            print(f"Step {i + 1}: {state}")

if __name__ == "__main__":
    solution = solve()
    print_solution(solution)
