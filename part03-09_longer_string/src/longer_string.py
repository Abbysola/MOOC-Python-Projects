# Write your solution here
str_a = input("Please type in string 1: ")
str_b = input("Please type in string 2: ")

if len(str_a) > len(str_b):
    print (f"{str_a} is longer")
elif len(str_b) > len(str_a):
    print (f"{str_b} is longer")
else:
    print("The strings are equally long")        