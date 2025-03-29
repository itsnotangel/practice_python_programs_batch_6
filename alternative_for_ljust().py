# Program 6: Add spaces to the end of a string to match a specified length without using ljust()

# Get user input
statement = input("Enter a statement: ")

# Add spaces to the end of the statement to match the specified length without using ljust()
padding_length = 10 # Desired length
if len(statement) < padding_length:
    statement += " " * (padding_length - len(statement))

# Display the result
print("Padded statement:'"+ statement , "'")