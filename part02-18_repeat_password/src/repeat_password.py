# Write your solution here
pw = input("Password: ")

while True:
    repeat_pw = input("Repeat password: ")
    if pw != repeat_pw:
        print ("They do not match!")
    else:
        break    
print ("User account created!")    