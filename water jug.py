from collections import deque

def water_jug_problem(capacity_A, capacity_B, target_C):
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        current_state = queue.popleft()

        if current_state[0] == target_C or current_state[1] == target_C:
            return current_state

        if current_state[0] < capacity_A:
            new_state = (capacity_A, current_state[1])
            if new_state not in visited:
                visited.add(new_state)
                queue.append(new_state)

       
        if current_state[1] < capacity_B:
            new_state = (current_state[0], capacity_B)
            if new_state not in visited:
                visited.add(new_state)
                queue.append(new_state)

5        if current_state[0] > 0:
            new_state = (0, current_state[1])
            if new_state not in visited:
                visited.add(new_state)
                queue.append(new_state)

        if current_state[1] > 0:
            new_state = (current_state[0], 0)
            if new_state not in visited:
                visited.add(new_state)
                queue.append(new_state)

        if current_state[0] > 0 and current_state[1] < capacity_B:
            pour = min(current_state[0], capacity_B - current_state[1])
            new_state = (current_state[0] - pour, current_state[1] + pour)
            if new_state not in visited:
                visited.add(new_state)
                queue.append(new_state)

    
        if current_state[1] > 0 and current_state[0] < capacity_A:
            pour = min(current_state[1], capacity_A - current_state[0])
            new_state = (current_state[0] + pour, current_state[1] - pour)
            if new_state not in visited:
                visited.add(new_state)
                queue.append(new_state)

    return None  

capacity_A = 4
capacity_B = 3
target_C = 2

result = water_jug_problem(capacity_A, capacity_B, target_C)

if result:
    print(f"Solution found: ({result[0]} liters in Jug A, {result[1]} liters in Jug B)")
else:
    print("No solution found.")
