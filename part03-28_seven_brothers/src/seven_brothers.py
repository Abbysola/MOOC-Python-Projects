# Write your solution here
# You can test your function by calling it within the following block
# if __name__ == "__main__":
#   seven_brothers()

def seven_brothers():
    brothers = ["Aapo", "Eero", "Juhani", "Lauri", "Simeoni", "Timo", "Tuomas"]
    brothers.sort()
    for brother in brothers:
        print(brother)

# Call the function to print the names of the seven brothers in alphabetical order

if __name__ == "__main__":
   seven_brothers()
    