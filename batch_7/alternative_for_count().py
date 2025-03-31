# Program 8: Count occurrences of a character in a string without using count()

# Get user input for the string and the character to search for
statement = input("Enter a statement: ")
char_to_count = input("Enter the character to count: ")

# Initialize a counter for the occurrences
count = 0

# Loop through each character in the string and check if it matches the target character
for char in statement:
    if char == char_to_count:
        count += 1

# Print the result
print("Number of occurences in the statement:", count)