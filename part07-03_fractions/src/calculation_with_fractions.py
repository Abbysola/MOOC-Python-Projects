# Write your solution here

from fractions import Fraction
 
def fractionate(amount: int):
    # numerator, denominator
    fraction = Fraction(1, amount)
 
    return [fraction] * amount

# Test the function


#print fractionate(5)
#[Fraction(1, 5), Fraction(1, 5), Fraction(1, 5), Fraction(1, 5), Fraction(1, 5)]