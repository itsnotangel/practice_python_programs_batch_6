# Program 3: Convert all characters to uppercase without using upper()

# Get user input
statement = input("Enter a statement: ")

# Convert to uppercase manually
uppercase_statement = "".join(chr(ord(char) - 32) if 'a' <= char <= 'z' else char for char in statement)

# Print the result
print(uppercase_statement)