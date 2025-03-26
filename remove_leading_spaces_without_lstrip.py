# Get input
# Remove leading spaces without using lstrip()
# Print output

user_input = input("Enter a statement with leading spaces: ")

processed_string = user_input.split(maxsplit=3)

print(processed_string)