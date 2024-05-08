# Write your solution here

word = input("Please type in a string: ") #rest

index = len(word)-1 #3

while index < len(word) and index >= 0:
    print(word[index])
    index -= 1