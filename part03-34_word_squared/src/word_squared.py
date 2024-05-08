# Write your solution here

def squared(text, num):
    n = -1
    length = len(text)
    for i in range(0, num):
        word = ""
        for i in range(0,num):
            index = n+1
            if index > length-1:
                index = index % length
            letter = text[index]
            word += letter
            n += 1
        print (word)

#This is what you will just be changing. The input        

# Test cases
if __name__ == "__main__":
    #squared("ab", 3)
    squared("aybabtu", 5)
