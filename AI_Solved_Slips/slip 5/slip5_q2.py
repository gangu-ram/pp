from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    def bfs(self, start, goal):
        visited = set()
        queue = deque([start])

        while queue:
            current_node = queue.popleft()
            if current_node in visited:
                continue

            visited.add(current_node)
            print(current_node, end=" ")

            if current_node == goal:
                print("\nGoal node reached!")
                return True

            neighbors = self.graph.get(current_node, [])
            queue.extend(neighbor for neighbor in neighbors if neighbor not in visited)

        print("\nGoal node not reached.")
        return False

# Example graph
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.add_edge(3, 5)
graph.add_edge(3, 6)
graph.add_edge(4, 2)
graph.add_edge(5, 7)
graph.add_edge(5, 8)
graph.add_edge(6, 8)
graph.add_edge(7, 8)

# Specify the initial and goal nodes
initial_node = 1
goal_node = 8

# Perform BFS
graph.bfs(initial_node, goal_node)
