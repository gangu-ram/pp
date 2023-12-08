from itertools import permutations

def solve_cryptarithmetic():
    # Define the letters in the cryptarithmetic problem
    letters = set('SENDMOREMONEY')
    
    # Generate all possible permutations of digits from 0 to 9 for the letters
    digit_permutations = permutations(range(10), len(letters))
    
    # Iterate through each permutation
    for perm in digit_permutations:
        digit_mapping = dict(zip(letters, perm))
        
        # Skip if any of the numbers start with a zero
        if digit_mapping['S'] == 0 or digit_mapping['M'] == 0:
            continue
        
        # Convert the words to numbers using the digit mapping
        send = digit_mapping['S'] * 1000 + digit_mapping['E'] * 100 + digit_mapping['N'] * 10 + digit_mapping['D']
        more = digit_mapping['M'] * 1000 + digit_mapping['O'] * 100 + digit_mapping['R'] * 10 + digit_mapping['E']
        money = digit_mapping['M'] * 10000 + digit_mapping['O'] * 1000 + digit_mapping['N'] * 100 + digit_mapping['E'] * 10 + digit_mapping['Y']
        
        # Check if the addition is correct
        if send + more == money:
            print("Solution found:")
            print(f"{digit_mapping['S']} {digit_mapping['E']} {digit_mapping['N']} {digit_mapping['D']}   (SEND)")
            print(f"+ {digit_mapping['M']} {digit_mapping['O']} {digit_mapping['R']} {digit_mapping['E']}   (MORE)")
            print("--------------")
            print(f"= {digit_mapping['M']} {digit_mapping['O']} {digit_mapping['N']} {digit_mapping['E']} {digit_mapping['Y']}   (MONEY)")
            print("\nWhere:")
            print(f"{send} + {more} = {money}")
            break
    else:
        print('No solution found')

if __name__ == "__main__":
    solve_cryptarithmetic()
