# write your solution here

with open("wordlist.txt") as file:
    dictionary = [word.replace("\n", "") for word in file]

sentence = input("Write text: ")
# split the text into words
check_words = sentence.split()
# check each word for spelling
corrected_text = []
for word in check_words:
    if word.lower() in dictionary:
        corrected_text.append(word)
    else:
        corrected_text.append(f"*{word}*")

print(' '.join(corrected_text))



