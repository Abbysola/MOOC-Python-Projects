# Write your solution here

def print_three_characters(string, char):
    index = string.find(char)  # Find the index of the specified character
    if index != -1 and index < len(string) - 2:
        print (string[index] + string[index+1] + string[index+2]) #(string[index:index+3]) 
        # Print the slice starting from the specified character
    else:
        print("")

# Get input from the user
user_string = input("Please type in a word: ")
user_char = input("Please type in a character: ")

# Call the function to print the first three characters slice
print_three_characters(user_string, user_char)
