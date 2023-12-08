from itertools import permutations

def is_valid_assignment(assignment):
    go, to, out = assignment
    return go + to == out

def solve_cryptarithmetic():
    letters = set("GTOU")
    for perm in permutations(range(10), len(letters)):
        assignment = dict(zip(letters, perm))
        go = assignment['G'] * 10 + assignment['O']
        to = assignment['T'] * 10 + assignment['O']
        out = assignment['O'] * 100 + assignment['U'] * 10 + assignment['T']
        
        if is_valid_assignment((go, to, out)):
            return {'GO': go, 'TO': to, 'OUT': out}

    return None

result = solve_cryptarithmetic()

if result:
    print("Solution found:")
    print("  GO:", result['GO'])
    print("  TO:", result['TO'])
    print("OUT:", result['OUT'])
else:
    print("No solution found.")
