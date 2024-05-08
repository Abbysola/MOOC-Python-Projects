# Write your solution here
n = int(input("Please type in a number: "))

if n < 10:
    print ("This number is smaller than 1000")
    print ("This number is smaller than 100")
    print ("This number is smaller than 10")
    print ("Thank you!")
elif n < 100:
    print ("This number is smaller than 1000")
    print ("This number is smaller than 100")
    print ("Thank you!")
elif n < 1000:
    print ("This number is smaller than 1000")
    print ("Thank you!")
else:
    print ("Thank you!")