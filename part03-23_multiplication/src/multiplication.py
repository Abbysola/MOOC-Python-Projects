# Write your solution here
def print_multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            result = i * j
            print(f"{i} x {j} = {result}")

# Get input from the user
number = int(input("Please type in a number: "))

# Print the multiplication table
print_multiplication_table(number)
       