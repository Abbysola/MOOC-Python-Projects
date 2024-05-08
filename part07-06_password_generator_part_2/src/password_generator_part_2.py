# Write your solution here

# If the second argument is True, the generated password should also contain one or more numbers.
# If the third argument is True, the generated password should also contain one or more of these 
# special characters: !?=+-()#.

import random
import string

def generate_strong_password(length, include_numbers=False, include_special_chars=False):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    numbers = string.digits
    special_chars = '!?=+-()#'

    # At least one lowercase letter is mandatory
    password = random.choice(lowercase_letters)

    # If include_numbers is True, include at least one number
    if include_numbers:
        password += random.choice(numbers)

    # If include_special_chars is True, include at least one special character
    if include_special_chars:
        password += random.choice(special_chars)

    # Fill up the rest of the password length with random characters
    remaining_length = length - len(password)
    for _ in range(remaining_length):
        char_pool = lowercase_letters + uppercase_letters
        if include_numbers:
            char_pool += numbers
        if include_special_chars:
            char_pool += special_chars
        password += random.choice(char_pool)

    # Shuffle the password to make it more random
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)

# Test the function

if __name__ == "__main__":
    for i in range(10):
       print(generate_strong_password(8, True, True))            