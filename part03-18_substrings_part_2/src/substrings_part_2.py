# Write your solution here
def print_substrings(string):
    length = len(string)
    for i in range(length, -1, -1):
        print(string[i:])

# Get input from the user
user_input = input("Please type in a string: ")

# Call the function to print substrings
print_substrings(user_input)