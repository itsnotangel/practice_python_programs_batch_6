# Program 7: Center a string by adding spaces without using center()

# Get user input
statement = input("Enter a statement: ")

# Add spaces at the beginning and end to center the text within a fixed width
width = 10
if len(statement) < width:
    total_padding = width - len(statement)
    left_padding = total_padding // 2
    right_padding = total_padding - left_padding
    statement = " " * left_padding + statement + " " * right_padding

# Display the result
print("Centered text:'" + statement + "'")