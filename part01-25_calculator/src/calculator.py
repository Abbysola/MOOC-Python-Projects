# Write your solution here
N1 = int(input("Number 1: "))
N2 = int(input("Number 2: "))
operation = str(input("Operation: "))

if operation == "add":
    print (f"{N1} + {N2} = {N1 + N2}")

elif operation == "multiply":
    print (f"{N1} * {N2} = {N1 * N2}")

elif operation == "subtract":
    print (f"{N1} - {N2} = {N1 - N2}")