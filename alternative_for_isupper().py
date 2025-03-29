# Program 4: Check if a string is uppercase without using isupper()

# Get user input
statement = input("Enter a statement: ")

# Check if all characters are uppercase without using isupper()
is_upper = True
for c in statement:
    if 'a' <= c <= 'z':
        is_upper = False
        break

# Display the result: Yes if all characters are uppercase, otherwise No
print("Is the statement in uppercase?:", "Yes" if is_upper else "No")