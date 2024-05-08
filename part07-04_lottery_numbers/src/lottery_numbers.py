# Write your solution here
import random

def lottery_numbers(amount: int, lower: int, upper: int):
    # Generate a list of unique random numbers within the specified range
    numbers = random.sample(range(lower, upper + 1), amount)
    # Sort the numbers in ascending order
    numbers.sort()
    return numbers     


if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
       print(number)     