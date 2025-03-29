# Program 5: Check if a string ends with a specific substring without using endswith()

# Step 1: Get user input
statement = input("Enter a statement: ")

# Step 2: Check if the statement ends with "ment" without using endswith()
suffix = "ment" # The suffix to check
if len(suffix) <= len(statement):
    statement_end = statement[-len(suffix):]
    ends_with = statement_end == suffix
else:
    ends_with = False

# Step 3: Display the result
print(ends_with)