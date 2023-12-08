from itertools import permutations

def is_valid_assignment(assignment, equation):
    for char in set(char for word in equation for char in word):
        if char in assignment and assignment[char] == '0':
            return False
    return True

def evaluate(equation, assignment):
    return int(''.join(assignment.get(char, '0') for char in equation))

def solve_cryptoarithmetic(equation):
    unique_chars = set(char for word in equation for char in word)
    digits = '0123456789'

    for perm in permutations(digits, len(unique_chars)):
        assignment = dict(zip(unique_chars, perm))
        if is_valid_assignment(assignment, equation) and \
           evaluate(equation[0], assignment) + evaluate(equation[1], assignment) == evaluate(equation[2], assignment):
            return assignment

    return None

def print_solution(equation, assignment):
    for word in equation:
        print(f"{word}: {''.join(assignment.get(char, '0') for char in word)}")
    print()

if __name__ == "__main__":
    equation = ['TWO', 'TWO', 'FOUR']
    solution = solve_cryptoarithmetic(equation)

    if solution:
        print("Solution found:")
        print_solution(equation, solution)
    else:
        print("No solution found.")
