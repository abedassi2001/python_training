class Graph:
    def __init__(self):
        self.adj_list = {}  # key: vertex, value: list of tuples (neighbor, weight)

    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, v1, v2, weight):
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.adj_list[v1].append((v2, weight))
        self.adj_list[v2].append((v1, weight))  # undirected graph

    def show_graph(self):
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex}: {neighbors}")

    def dfs(self, root, visited=None):
        if visited is None:
            visited = set()
        visited.add(root)
        print(root, end=" ")
        for neighbor, _ in self.adj_list[root]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def find_max_edge(self, root, visited=None):
        if visited is None:
            visited = set()
        visited.add(root)

        max_edge = 0
        for neighbor, weight in self.adj_list[root]:
            max_edge = max(max_edge, weight)
            if neighbor not in visited:
                max_edge = max(max_edge, self.find_max_edge(neighbor, visited))
        return max_edge
g = Graph()
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 2)
g.add_edge(1, 3, 7)
g.add_edge(2, 3, 3)

print("Graph adjacency list:")
g.show_graph()

print("\nDFS traversal from vertex 0:")
g.dfs(0)

print("\nMaximum edge weight in the graph:", g.find_max_edge(0))
