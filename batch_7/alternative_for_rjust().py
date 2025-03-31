# Program 6: Add leading spaces without using rjust()

# Get user input
statement = input("Enter a statement: ")
width = int(input("Enter the total width: "))

# Manually add leading spaces
if len(statement) < width:
    spaces = " " * (width - len(statement))
    right_justified_statement = spaces + statement
else:
    right_justified_statement = statement

# Print the result
print(right_justified_statement)