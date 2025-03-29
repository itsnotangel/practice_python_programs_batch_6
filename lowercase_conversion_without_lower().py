# Program 3: Convert string to lowercase without using lower()

# Step 1: Get user input
statement = input("Enter a statement: ")

# Step 2: Convert to lowercase without using lower()
result = "".join(chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in statement)

# Step 3: Display the result
print(result)