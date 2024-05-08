# Write your solution here

limit = int(input("Limit: "))
value = 1
sum_of_values = 0

while sum_of_values < limit: 
    sum_of_values += value
    value += 1

print (sum_of_values)    
