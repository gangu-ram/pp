import calendar

# Get user input for the year and month
y = int(input("Enter the year: "))
m = int(input("Enter the month (1-12): "))

# Print the calendar for the specified year and month
print(calendar.month(y, m))
