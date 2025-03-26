# Get input
# Remove leading spaces without using lstrip()
# Print output

user_input = input("Enter a statement with leading spaces: ")

processed_string = " ".join(user_input.split(maxsplit=1))  

print(processed_string)