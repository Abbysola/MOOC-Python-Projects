from math import sqrt
# Write your solution here

number = int(input("Please type in a number: "))

while number > 0:
    print (sqrt(number))
    number = int(input("Please type in a number: "))
    if number < 0:
        print ("Invalid number")
        number = int(input("Please type in a number: "))
    elif number == 0:
        break
print ("Exiting...")
