# Program 10: Capitalize the first letter of each word in a string without using title()

# Get user input
statement = input("Enter a statement: ")

# Capitalize the first letter of each word and make all others lowercase
result = " ".join(word[0].upper() + word[1:].lower() if word else "" for word in statement.split())

# Display the result
print(result)