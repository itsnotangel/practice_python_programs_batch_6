# Program 5: Check if a string ends with a specific substring without using endswith()

# Get user input
statement = input("Enter a statement: ")

# Check if the statement ends with "ment" without using endswith()
suffix = "ment" # The suffix to check
if len(suffix) <= len(statement):
    statement_end = statement[-len(suffix):]
    ends_with = statement_end == suffix
else:
    ends_with = False

# Display the result
print("Does it end with 'ment'?:", "Yes" if ends_with else "No")