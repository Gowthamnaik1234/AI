def is_valid_assignment(graph, assignment, node, color):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtracking(graph, colors, assignment, node):
    if node not in assignment:
        for color in colors:
            if is_valid_assignment(graph, assignment, node, color):
                assignment[node] = color
                if len(assignment) == len(graph):
                    return True
                next_node = get_unassigned_node(graph, assignment)
                if backtracking(graph, colors, assignment, next_node):
                    return True
                assignment.pop(node)
    return False

def get_unassigned_node(graph, assignment):
    for node in graph:
        if node not in assignment:
            return node

def map_coloring(graph, colors):
    assignment = {}
    start_node = get_unassigned_node(graph, assignment)
    if backtracking(graph, colors, assignment, start_node):
        return assignment
    else:
        return None

if __name__ == "__main__":
    # Define the graph (adjacency list)
    graph = {
        "WA": ["NT", "SA"],
        "NT": ["WA", "SA", "Q"],
        "SA": ["WA", "NT", "Q", "NSW", "V"],
        "Q": ["NT", "SA", "NSW"],
        "NSW": ["Q", "SA", "V"],
        "V": ["SA", "NSW"]
    }

    # Define the available colors
    colors = ["Red", "Green", "Blue"]

    # Solve the map coloring problem
    solution = map_coloring(graph, colors)

    if solution:
        print("Map coloring solution:")
        for node, color in solution.items():
            print(f"{node}: {color}")
    else:
        print("No solution exists.")

