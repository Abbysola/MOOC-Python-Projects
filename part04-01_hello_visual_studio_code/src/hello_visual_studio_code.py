# Write your solution here


while True:
    editor = input("Editor: ")
    editor = editor.lower()
    if editor == "word" or editor == "notepad":
       print ("awful")
    elif editor != "visual studio code":
       print ("not good")
    elif editor == "visual studio code":
            break 
print("an excellent choice!")         