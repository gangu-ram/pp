from itertools import permutations

def solve_cryptarithmetic():
    # Define the letters in the cryptarithmetic problem
    letters = set('CROSSROADSDANGER')
    
    # Generate all possible permutations of digits from 0 to 9 for the letters
    digit_permutations = permutations(range(10), len(letters))
    
    # Iterate through each permutation
    for perm in digit_permutations:
        digit_mapping = dict(zip(letters, perm))
        
        # Skip if any of the numbers start with a zero
        if digit_mapping['C'] == 0 or digit_mapping['R'] == 0 or digit_mapping['D'] == 0:
            continue
        
        # Convert the words to numbers using the digit mapping
        cross = digit_mapping['C'] * 1000 + digit_mapping['R'] * 100 + digit_mapping['O'] * 10 + digit_mapping['S']
        roads = digit_mapping['R'] * 1000 + digit_mapping['O'] * 100 + digit_mapping['A'] * 10 + digit_mapping['D']
        danger = digit_mapping['D'] * 100000 + digit_mapping['A'] * 10000 + digit_mapping['N'] * 1000 + digit_mapping['G'] * 100 + digit_mapping['E'] * 10 + digit_mapping['R']
        
        # Check if the addition is correct
        if cross + roads == danger:
            print("Solution found:")
            print(f"{digit_mapping['C']} {digit_mapping['R']} {digit_mapping['O']} {digit_mapping['S']} {digit_mapping['S']}  (CROSS)")
            print(f"+ {digit_mapping['R']} {digit_mapping['O']} {digit_mapping['A']} {digit_mapping['D']} {digit_mapping['S']}  (ROADS)")
            print("--------------")
            print(f"= {digit_mapping['D']} {digit_mapping['A']} {digit_mapping['N']} {digit_mapping['G']} {digit_mapping['E']} {digit_mapping['R']}  (DANGER)")
            print("\nWhere:")
            print(f"{cross} + {roads} = {danger}")
            break
    else:
        print('No solution found')

if __name__ == "__main__":
    solve_cryptarithmetic()
