# Write your solution here
def chessboard(length):
    for i in range(length):
        row = ""
        for j in range(length):
            if (i + j) % 2 == 0:
                row += "1"
            else:
                row += "0"
        print(row)
# Testing the function
if __name__ == "__main__":
    chessboard(3)
