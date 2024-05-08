# Write your solution here
number = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))

groups = number % group_size

if groups == 0:
   print (f"Number of groups formed: {number//group_size}")
else:
   print (f"Number of groups formed: {(number//group_size)+1}")