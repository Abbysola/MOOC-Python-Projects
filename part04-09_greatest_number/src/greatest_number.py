# Write your solution here
def greatest_number(a,b,c):
    d = [a,b,c]
    d.sort()
    A = d[-1]
    return A


# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)