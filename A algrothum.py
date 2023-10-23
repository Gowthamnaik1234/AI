import heapq

class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def astar_search(start_state, goal_state, actions, cost, heuristic):
    open_set = []
    closed_set = set()

    start_node = Node(start_state, None, 0, heuristic(start_state, goal_state))
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)
        current_state = current_node.state

        if current_state == goal_state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return list(reversed(path))

        closed_set.add(current_state)

        for action in actions(current_state):
            next_state = action
            if next_state in closed_set:
                continue

            tentative_cost = current_node.cost + cost(current_state, next_state)
            next_node = Node(next_state, current_node, tentative_cost, heuristic(next_state, goal_state))

            if not any(node.cost < next_node.cost and node.state == next_state for node in open_set):
                heapq.heappush(open_set, next_node)

    return None

# Example usage:
def actions(state):
    x, y = state
    possible_moves = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    return [(x, y) for x, y in possible_moves if 0 <= x < 5 and 0 <= y < 5]

def cost(state1, state2):
    return 1

def heuristic(state, goal):
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])

start_state = (0, 0)
goal_state = (4, 4)

path = astar_search(start_state, goal_state, actions, cost, heuristic)
if path:
    print("Shortest path from", start_state, "to", goal_state, "is:", path)
else:
    print("No path found.")
