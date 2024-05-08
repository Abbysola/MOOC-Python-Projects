# Copy here code of line function from previous exercise

def line(val, str):
    if str == "":
        print ("*" * val)
    elif str != "":
        print (str[0] * val) 

def box_of_hashes(height):
    for i in range(height):
        line(10, "#")
    # You should call function line here with proper parameters
      
# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
