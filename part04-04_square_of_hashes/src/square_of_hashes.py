# Copy here code of line function from previous exercise

def line(val, str):
    if str == "":
        print ("*" * val)
    elif str != "":
        print (str[0] * val)

def square_of_hashes(size):
    for i in range(size):     
    # You should call function line here with proper parameters
        line(size, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
