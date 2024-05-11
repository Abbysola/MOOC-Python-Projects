# Write your solution here

sentence = []
count = 0
while True:
    word = input("Word: ")
    if word in sentence:   
        break 
    else:
        sentence.append(word)
        count += 1
    
print(f"You typed in {count} different words") 

