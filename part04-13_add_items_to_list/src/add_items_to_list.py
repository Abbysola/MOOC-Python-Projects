# Write your solution here


quantity = int(input("How many items: "))
my_list = []

for i in range(1,quantity+1):
    item = int(input(f"Item {i}: "))
    my_list.append(item)

print(my_list)