# Copy here code of line function from previous exercise and use it in your solution
def line(val, str):
    if str == "":
        print ("*" * val)
    elif str != "":
        print (str[0] * val)

def shape(w, char_t, h, char_r):
    for i in range(w+1):
    # You should call function line here with proper parameters
       line(i, char_t)
    for j in range(h):
    # You should call function line here with proper parameters
        line(w, char_r) 
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")