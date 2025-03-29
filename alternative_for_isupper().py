# Program 4: Check if a string is uppercase without using isupper()

# Step 1: Get user input
statement = input("Enter a statement: ")

# Step 2: Check if all characters are uppercase without using isupper()
is_upper = True
for c in statement:
    if 'a' <= c <= 'z':
        is_upper = False
        break

# Step 3: Display the result
print(is_upper)
