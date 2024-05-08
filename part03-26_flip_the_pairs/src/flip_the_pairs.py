def print_flipped_pairs(number):
    for i in range(2, number + 1, 2):
        print(i)
        if i - 1 <= number:
            print(i - 1)   
    if number % 2 != 0:
        print(number)
        
# Get input from the user
number = int(input("Please type in a number: "))

# Print the flipped pairs
print_flipped_pairs(number)     
