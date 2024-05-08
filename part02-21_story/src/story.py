# Write your solution here
previous_word = None
word = None
words = ""

while True:
    previous_word = word
    word = input("Please type in a word: ")
    
    if word == previous_word or word == "end":
        print(words)
        break
    else:
        words += word + " "    


    




        


