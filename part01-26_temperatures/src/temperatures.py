# Write your solution here
fah_temp = int(input("Please type in a temperature: "))

cel_temp = (fah_temp - 32) * 5/9

if cel_temp < 0:
    print (f"{fah_temp} degrees Fahrenheit equals {cel_temp} degrees Celsius")
    print ("Brr! It's cold in here!")

else:
    print (f"{fah_temp} degrees Fahrenheit equals {cel_temp} degrees Celsius")