# Write your solution here
string = input("Please type in a word: ")
char = input("Please type in a character: ") 
   
index = string.find(char)

while index != -1 and index < len(string) - 2:
    print (string[index:index+3]) 
    index = string.find(char, index + 1)
    
            