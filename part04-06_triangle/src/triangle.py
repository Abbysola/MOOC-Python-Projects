# Copy here code of line function from previous exercise
def line(val, str):
    if str == "":
        print ("*" * val)
    elif str != "":
        print (str[0] * val)

def triangle(size):
    for i in range(size+1):
    # You should call function line here with proper parameters
       line(i, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
