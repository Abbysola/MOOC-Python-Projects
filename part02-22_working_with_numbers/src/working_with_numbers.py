# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
count = 0
count_pos = 0
count_neg = 0
sum_of_num = 0

while True:
    num = int(input("Number: "))
    if num != 0:
        count += 1
        sum_of_num += num
        if num > 0:
            count_pos += 1
        elif num < 0:
            count_neg += 1
    elif num == 0:
        break  

print (f"Numbers typed in {count}")
print (f"The sum of the numbers is {sum_of_num}")
print (f"The mean of the numbers is {(sum_of_num/count)}")
print (f"Positive numbers {count_pos}")
print (f"Negative numbers {count_neg}") 
                     

