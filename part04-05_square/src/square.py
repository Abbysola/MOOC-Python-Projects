# Copy here code of line function from previous exercise
def line(val, str):
    if str == "":
        print ("*" * val)
    elif str != "":
        print (str[0] * val)
        
def square(size, character):
    for i in range(size):
    # You should call function line here with proper parameters
        line(size, character)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")