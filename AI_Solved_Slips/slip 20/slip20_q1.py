class CollegeBot:
    def __init__(self):
        self.college_info = {
            "name": "Awesome University",
            "location": "Cityville",
            "founded": 1990,
            "majors": ["Computer Science", "Business Administration", "Biology"],
            "total_students": 5000,
            "website": "http://www.awesomeuniversity.edu",
        }

    def get_info(self, query):
        query = query.lower()

        if "name" in query:
            return f"The college's name is {self.college_info['name']}."
        elif "location" in query:
            return f"It is located in {self.college_info['location']}."
        elif "founded" in query:
            return f"The college was founded in {self.college_info['founded']}."
        elif "majors" in query:
            return f"The college offers majors in {', '.join(self.college_info['majors'])}."
        elif "total students" in query:
            return f"The total number of students in the college is {self.college_info['total_students']}."
        elif "website" in query:
            return f"You can visit the college's website at {self.college_info['website']}."
        else:
            return "I'm sorry, I don't have information on that topic."

def main():
    bot = CollegeBot()

    print("Welcome to CollegeBot! Ask me about your college.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Goodbye!")
            break

        response = bot.get_info(user_input)
        print("CollegeBot:", response)

if __name__ == "__main__":
    main()
