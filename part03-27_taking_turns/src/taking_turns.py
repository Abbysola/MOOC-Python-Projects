# Write your solution here

#num = int(input("Please type in a number:"))
#number_list = [i+1 for i in range(num)]

#while number_list:
#    print(number_list.pop(0))
 #   number_list.reverse()

num = int(input("Please type in a number:"))
nums = list(range(1, num+1))
while nums:
    print(nums.pop(0))
    if nums:  
       print(nums.pop())    
    
