# Program 9: Capitalize the first letter of a string without using capitalize()

# Get user input
statement = input("Enter a statement: ")

# Capitalize the first letter and make all others lowercase
result = (statement[0].upper() + statement[1:].lower()) if statement else statement

# Display the result
print(result)