# Write your solution here
from math import sqrt
def hypotenuse(leg1: float, leg2: float):
    hyp = (leg1 ** 2 + leg2 ** 2) ** 0.5
    return hyp

if __name__ == "__main__":
    print(hypotenuse(3,4))
