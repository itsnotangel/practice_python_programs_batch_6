# Program 7: Add leading zeros without using zfill()

# Get input from the user
number = input("Enter a number: ")

# Assigned number to be padded with leading zeros
width = 8

# Add leading zeros manually
if len(number) < width:
    number = '0' * (width - len(number)) + number

# Print the result
print(number)