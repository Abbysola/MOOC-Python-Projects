# Write your solution here
limit = int(input("Limit: "))
value = 1
sum_of_values = 0
values = ""

while sum_of_values < limit: 
    sum_of_values += value
    values += f"{value} + "
    value += 1

values = values[:-2]    
    
print (f"The consecutive sum: {values} = {sum_of_values}")  