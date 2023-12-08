import heapq
import copy

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost
        self.heuristic = self.calculate_heuristic()

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(tuple(map(tuple, self.state)))

    def is_goal(self):
        return self.state == goal_state

    def calculate_heuristic(self):
        return sum(abs(i - goal_positions[value][0]) + abs(j - goal_positions[value][1])
                   for i, row in enumerate(self.state) for j, value in enumerate(row) if value != 0)

    def generate_children(self):
        empty_position = next((i, j) for i, row in enumerate(self.state) for j, value in enumerate(row) if value == 0)

        moves = possible_moves.get(empty_position, [])
        return [PuzzleNode(self.make_move(empty_position, move), parent=self, move=move, cost=self.cost + 1)
                for move in moves]

    def make_move(self, empty_position, move):
        i, j = empty_position
        new_state = copy.deepcopy(self.state)

        if move == 'up' and i > 0:
            new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], new_state[i][j]
        elif move == 'down' and i < 2:
            new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], new_state[i][j]
        elif move == 'left' and j > 0:
            new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]
        elif move == 'right' and j < 2:
            new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]

        return new_state


def a_star(initial_state):
    initial_node = PuzzleNode(initial_state)
    heap = [initial_node]
    heapq.heapify(heap)
    visited = set()

    while heap:
        current_node = heapq.heappop(heap)

        if current_node.is_goal():
            return current_node

        visited.add(current_node)

        children = current_node.generate_children()
        for child in children:
            if child not in visited:
                heapq.heappush(heap, child)

    return None


def print_solution(solution_node):
    path = []
    while solution_node:
        path.append((solution_node.move, solution_node.state))
        solution_node = solution_node.parent

    path.reverse()
    for move, state in path:
        print(f"Move {move}:\n{state[0]}\n{state[1]}\n{state[2]}\n")


def get_user_input():
    print("Enter the initial state (use 0 for the blank space):")
    initial_state = [list(map(int, input().split())) for _ in range(3)]

    print("Enter the goal state:")
    goal_state = [list(map(int, input().split())) for _ in range(3)]

    return initial_state, goal_state


initial_state, goal_state = get_user_input()

goal_positions = {value: (i, j) for i, row in enumerate(goal_state) for j, value in enumerate(row)}
possible_moves = {(i, j): ['up', 'down', 'left', 'right'] for i in range(3) for j in range(3)}

solution_node = a_star(initial_state)

if solution_node:
    print("Solution found!")
    print_solution(solution_node)
else:
    print("No solution found.")
