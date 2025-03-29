# Program 2: Remove prefix from a string without using removeprefix()

# Prompt user to enter a statement
statement = input("Enter a statement with a prefix: ")

# Remove first character if not empty then print the string without prefix
print("String without prefix:", statement[1:] if statement else statement)