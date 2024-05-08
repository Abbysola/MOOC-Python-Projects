# Write your solution here
def middle_letter(letter1, letter2, letter3):
    letters = [letter1, letter2, letter3]
    letters.sort()
    return letters[1]

letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")

result = middle_letter(letter1, letter2, letter3)
print(f"The letter in the middle is {result}")