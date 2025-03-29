# Program 8: Swap the casing of each character in a string without using swapcase()

# Step 1: Get user input
statement = input("Enter a statement: ")

# Step 2: Reverse the casing of each character without using swapcase()
result = ""
for c in statement:
    if 'a' <= c <= 'z':
        result += chr(ord(c) - 32)
    elif 'A' <= c <= 'Z':
        result += chr(ord(c) + 32)
    else:
        result += c

# Step 3: Display the result
print("Swapped case string:", result)