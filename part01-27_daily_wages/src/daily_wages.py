# Write your solution here
wage = float(input("Hourly wage: "))
hours = float(input("Hours worked: "))
day = str(input("Day of the week: "))

daily_wages = wage * hours
daily_wages_sun = wage * 2 * hours

if day == "Sunday":
    print (f"Daily wages: {daily_wages_sun} euros")
else:
    print (f"Daily wages: {daily_wages} euros")    
