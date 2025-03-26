# Program 1: Remove leading spaces without using lstrip().

# Prompt user for input
user_input = input("Enter a statement with leading spaces: ")

# Splits input into at most two parts and joins them back to remove leading spaces
processed_string = " ".join(user_input.split(maxsplit=1))  

# Display the result
print("Without leading space:", processed_string)