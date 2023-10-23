class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
    
    def dfs_recursive(self, node, visited):
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            if node in self.graph:
                for neighbor in self.graph[node]:
                    self.dfs_recursive(neighbor, visited)

    def dfs(self, start_node):
        visited = set()
        self.dfs_recursive(start_node, visited)

# Example usage:
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("DFS starting from node 2:")
    g.dfs(2)
