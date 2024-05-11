# Write your solution here

my_list = []
print (f"The list is now {my_list}") 
while True: 
    operation = input("a(d)d, (r)emove or e(x)it: ")
    if operation == "d":
        if not my_list: 
          my_list.append(1)  
        elif my_list:
          my_list.append(my_list[-1]+1)
    elif operation == "r":
        if my_list:
            my_list.pop(-1)
    elif operation == "x":
        print ("Bye!")
        break
    print (f"The list is now {my_list}")

