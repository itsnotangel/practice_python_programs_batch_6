# Program 4: Check if all characters are lowercase without using islower()

# Get input from the user
statement = input("Enter a statement: ")

# Print the question
print("Is the statement all lowercase?")

# Check if all characters are lowercase manually
if all('a' <= char <= 'z' or not char.isalpha() for char in statement):
    print("Yes")
else:
    print("No")