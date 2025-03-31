# Program 5: Check if string starts with a substring without using startswith()

# Get input from the user
statement = input("Enter a statement: ")

# Assigned substring to check
substring = input("Enter the substring to check for: ")

# Check if the string starts with the substring manually
if statement[:len(substring)] == substring:
    print("Yes")
else:
    print("No")