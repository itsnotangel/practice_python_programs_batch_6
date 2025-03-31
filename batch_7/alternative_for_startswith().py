# Program 5: Check if string starts with a substring without using startswith()

# Get input from the user
statement = input("Enter a statement: ")

# Assigned substring to check
substring = input("Enter the substring to check for: ")

# Check if the string starts with the substring manually
if statement[:len(substring)] == substring:
    print("The statement starts with" , substring + ".")
else:
    print("The statement does not start with", substring + ".")