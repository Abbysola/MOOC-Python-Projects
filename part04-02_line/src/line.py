# Write your solution here
def line(val, str):
    if str == "":
        print ("*" * val)
    elif str != "":
        print (str[0] * val)   
    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")