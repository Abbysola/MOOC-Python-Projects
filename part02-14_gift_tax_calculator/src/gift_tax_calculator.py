# Write your solution here
def calculate_gift_tax(gift_amount):
    if 5000 <= gift_amount <= 25000:
        tax = 100 + (gift_amount - 5000) * 0.08
        return tax
    elif 25000 <= gift_amount <= 55000:
        tax = 1700 + (gift_amount - 25000) * 0.10
        return tax
    elif 55000 <= gift_amount <= 200000:
        tax = 4700 + (gift_amount - 55000) * 0.12
        return tax
    elif 200000 <= gift_amount <= 1000000:
        tax = 22100 + (gift_amount - 200000) * 0.15
        return tax
    elif gift_amount > 100000:
        tax = 142100 + (gift_amount - 1000000) * 0.17
        return tax
    elif gift_amount < 5000:
        return 0

gift_amount = float(input("Value of gift: "))
tax_amount = calculate_gift_tax(gift_amount)
if tax_amount != 0:
    print(f"Amount of tax: {tax_amount} euros")
else:
    print ("No tax!")    