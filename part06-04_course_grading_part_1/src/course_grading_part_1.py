# write your solution here
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

names = {}

with open(student_info) as file:
    for line in file:
        items = line.replace("\n","").split(";")
        if items[0] == "id":
            continue
        names[items[0]] = items[1] + " " + items[2]

scores = {} 

with open(exercise_data) as file:
    for line in file:
        items = line.replace("\n","").split(";")
        if items[0] == "id":
            continue
        score_sum = 0
        for i in range(1,8):
            score_sum += int(items[i])
        scores[items[0]] = score_sum    
        #scores[items[0]] = int(items[1])+int(items[2])+int(items[3])+int(items[4])+int(items[5])+int(items[6])+int(items[7])

#for id, name in names.items():
#    if id in scores:
#       score = scores[id]
#        print (f"{name} {score}") 

for id, name in names.items():
    print(f"{name} {scores[id]}")     
       



