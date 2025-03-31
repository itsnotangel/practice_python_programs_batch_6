# Program 9: Find the index of the first occurrence of a character without using index()

# Get user input
statement = input("Enter a statement: ")

# Check the location of the parameter in the string
for i, char in enumerate(statement):
    if char == "w":
        index = i
        break

# Print the result
print("The first occurence is at:", index)