# Write your solution here
count = 1

while True:
    pin = int(input("PIN: "))
    if pin != 4321:
       print ("Wrong")
       count += 1
    else:
        break
if count == 1:        
    print (f"Correct! It only took you one single attempt!") 
elif count > 0:
    print (f"Correct! It took you {count} attempts")    
