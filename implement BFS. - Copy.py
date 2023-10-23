from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = deque()
        result = []

        queue.append(start)
        visited.add(start)

        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        return result

if __name__ == "__main__":
    # Create a sample graph
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    start_node = 2  # Starting node for BFS traversal

    print("Breadth-First Search starting from node", start_node)
    result = graph.bfs(start_node)
    print("BFS traversal result:", result)
