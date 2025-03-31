# Program 10: Find the last occurrence index without using rindex()

# Get input from user
statement = input("Enter a statement: ")
char_to_find = input("Enter the character to find: ")

# Manually find the last occurrence index
last_index = -1
for i in range(len(statement) - 1, -1, -1):
    if statement[i] == char_to_find:
        last_index = i
        break

# Print the result
print("Last occurrence index:", last_index)
