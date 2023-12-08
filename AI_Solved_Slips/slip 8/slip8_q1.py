def count_upper_lower(string):
    # Initialize counters
    upper_count = 0
    lower_count = 0

    # Iterate through each character in the string
    for char in string:
        # Check if the character is an uppercase alphabet
        if char.isupper():
            upper_count += 1
        # Check if the character is a lowercase alphabet
        elif char.islower():
            lower_count += 1

    # Print the results
    print("Number of uppercase alphabets:", upper_count)
    print("Number of lowercase alphabets:", lower_count)

if __name__ == "__main__":
    # Accept a string from the user
    user_input = input("Enter a string: ")

    # Call the function to count uppercase and lowercase alphabets
    count_upper_lower(user_input)
