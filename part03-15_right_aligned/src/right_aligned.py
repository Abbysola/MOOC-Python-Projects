# Write your solution here

str_input = input("Please type in a string: ")

stars = ("*" * (20 - len(str_input)))
output = stars + str_input

print (output)