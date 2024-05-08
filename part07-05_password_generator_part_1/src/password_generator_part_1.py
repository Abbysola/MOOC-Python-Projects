# Write your solution here
from random import choice
from string import ascii_lowercase 
def generate_password(length: int):
    passwd = ""
    for i in range(length):
        passwd += choice(ascii_lowercase)
 
    return passwd

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))    
        