# Write your solution here
count = float(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
groceries = float(input("How much money do you spend on groceries in a week? "))
print ("")
print("Average food expenditure: ")
print (f"Daily: {((count * price) + groceries) / 7} euros")
print (f"Weekly: {(count * price)+ groceries} euros")