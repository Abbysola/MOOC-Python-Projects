# Write your solution here

#same letter at index b and c = true
#difft letters at index b and c = false
#either index b or c fall outside the scope

def same_chars(string, index1, index2):
    if 0 <= index1 < len(string) and 0 <= index2 < len(string):
        return string[index1] == string[index2]
    else:
        return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))