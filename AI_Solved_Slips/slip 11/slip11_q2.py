from collections import deque

def water_jug_solution(a, b, target):
    visited_states = set()
    is_solvable = False
    path = []

    queue = deque()
    queue.append((0, 0))

    while queue:
        u = queue.popleft()

        if tuple(u) in visited_states:
            continue

        if u[0] > a or u[1] > b or u[0] < 0 or u[1] < 0:
            continue

        path.append([u[0], u[1]])
        visited_states.add(tuple(u))

        if u[0] == target or u[1] == target:
            is_solvable = True

            if u[0] == target:
                if u[1] != 0:
                    path.append([u[0], 0])
            else:
                if u[0] != 0:
                    path.append([0, u[1]])

            for state in path:
                print("(", state[0], ",", state[1], ")")

            break

        queue.append((u[0], b))  # Fill Jug2
        queue.append((a, u[1]))  # Fill Jug1

        for ap in range(max(a, b) + 1):
            c, d = u[0] + ap, u[1] - ap

            if c == a or (d == 0 and d >= 0):
                queue.append((c, d))

            c, d = u[0] - ap, u[1] + ap

            if (c == 0 and c >= 0) or d == b:
                queue.append((c, d))

        queue.append((a, 0))
        queue.append((0, b))

    if not is_solvable:
        print("Solution not possible")

if __name__ == '__main__':
    jug1, jug2, target = 4, 3, 2
    print("Path from initial state to solution state:")
    water_jug_solution(jug1, jug2, target)
