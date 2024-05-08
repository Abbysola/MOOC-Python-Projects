# Write your solution here
temp_ans = ["Wear jeans and a T-shirt", "I recommend a jumper as well", "Take a jacket with you", "Make it a warm coat, actually", "I think gloves are in order"]
rain_ans = ["Don't forget your umbrella!"]
#repeat = True


#def weather_forecast():
    #using .int() to convert to integer
temp_q = input("What is the weather forecast for tomorrow?\n Temperature:")
temp_q = int(temp_q)
rain_q = input("Will it rain?").lower()

if temp_q >= 21:
    print(temp_ans[0])
                
if temp_q >= 11 and temp_q < 21:
    print(temp_ans[0])
    print(temp_ans[1])
        
if temp_q >= 7 and temp_q < 11:
    print(temp_ans[0])
    print(temp_ans[1])
    print(temp_ans[2])
            
if temp_q < 7:
    print(temp_ans[0])
    print(temp_ans[1])
    print(temp_ans[2])
    print(temp_ans[3])
    print(temp_ans[4])
    
if rain_q == "yes":
    print(rain_ans[0])
        
#while repeat:  
    #weather_forecast()
    #cont = input("\nWant a cloth guide again?").lower()
    #if cont == "no":
        #repeat = False