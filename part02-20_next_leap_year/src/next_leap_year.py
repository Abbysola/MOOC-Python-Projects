# Write your solution here
year = int(input("Year: "))
next_year = year + 1

while True:
    if (next_year % 4 == 0 and next_year % 100 != 0) or (next_year % 400 == 0):
        print (f"The next leap year after {year} is {next_year}") 
        break
    else:    
        next_year += 1

