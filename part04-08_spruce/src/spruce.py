# Write your solution here

def spruce(size): #3
    print("a spruce!")
    for i in range(1, size + 1):  #1
        print(" " * (size - i) + "*" * (2 * i - 1)) #2 spaces * #1 space *** #0 space *****
    print(" " * (size - 1) + "*") 

# Test the function
spruce(3)
       
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)