class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    def dfs(self, start, goal):
        visited = set()

        def dfs_recursive(node):
            visited.add(node)
            print(node, end=" ")

            if node == goal:
                print("\nGoal node reached!")
                return True

            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    if dfs_recursive(neighbor):
                        return True

            return False

        if start not in self.graph:
            print("Start node not found in the graph.")
            return

        print("Depth First Search:")
        dfs_recursive(start)

# Example graph
graph = Graph()
graph.add_edge(1, 3)
graph.add_edge(1, 2)
graph.add_edge(2, 4)
#graph.add_edge(2, 5)
graph.add_edge(3, 2)
#graph.add_edge(3, 7)
graph.add_edge(4, 5)
graph.add_edge(4, 6)
graph.add_edge(5, 3)
graph.add_edge(5, 7)
#graph.add_edge(6, 8)
graph.add_edge(7, 6)

# Specify the initial and goal nodes
initial_node = 1
goal_node = 7

# Perform DFS
graph.dfs(initial_node, goal_node)
