import random
import re

def simple_chatbot(user_input):
    # Define patterns and responses
    patterns_responses = {
        r"(hello|hi|hey|good morning|good afternoon|good evening)": ["Hello!", "Hi there!", "Hey!"],
        r"how are you": ["I'm good, thank you!", "I'm doing well, how about you?"],
        r"what is your name": ["I'm a simple chatbot.", "You can call me ChatBot."],
        r"bye|goodbye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
        r"what is your age":["I m robot i dont have age"],
        # Add more patterns and responses as needed
    }

    # Iterate through patterns and find a match
    for pattern, responses in patterns_responses.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return random.choice(responses)

    # If no match is found, provide a default response
    return "I'm not sure how to respond to that."

# Simple chatbot loop
print("Simple ChatBot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    
    # Exit the loop if the user types 'bye'
    if user_input.lower() == 'bye':
        print("Simple ChatBot: Goodbye!")
        break

    response = simple_chatbot(user_input)
    print("Simple ChatBot:", response)
