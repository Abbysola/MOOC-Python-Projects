# wwite your solution here
#if False:
    # this is never executed
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")
#else:
    # hard-coded input
    #student_info = "students4.csv"
    #exercise_data = "exercises4.csv"
    #exam_points = "exam_points4.csv"

names = {}

with open(student_info) as file:
    for line in file:
        items = line.replace("\n","").split(";")
        if items[0] == "id":
            continue
        names[items[0]] = items[1] + " " + items[2]

exercises = {} 

with open(exercise_data) as file:
    for line in file:
        items = line.replace("\n","").split(";")
        if items[0] == "id":
            continue
        exercises_sum = 0
        for i in range(1,8):
            exercises_sum += int(items[i])
        #exercises[items[0]] = exercise_sum 
        #calculating percentage base on total exercises done
        exercise_percent = (exercises_sum/40) * 100
        #calculating exercise points gotten based on percentage
        if exercise_percent < 10:
            exercises[items[0]] = 0
        if exercise_percent >= 10:
            exercises[items[0]] = 1   
        if exercise_percent >= 20:  
            exercises[items[0]] = 2
        if exercise_percent >= 30:  
            exercises[items[0]] = 3
        if exercise_percent >= 40:  
            exercises[items[0]] = 4
        if exercise_percent >= 50:  
            exercises[items[0]] = 5
        if exercise_percent >= 60:  
            exercises[items[0]] = 6
        if exercise_percent >= 70:  
            exercises[items[0]] = 7
        if exercise_percent >= 80:  
            exercises[items[0]] = 8
        if exercise_percent >= 90:  
            exercises[items[0]] = 9
        if exercise_percent == 100:  
            exercises[items[0]] = 10

exams = {}
with open(exam_points) as file:
    for line in file:
        items = line.replace("\n","").split(";")
        if items[0] == "id":
            continue
        exam_points_sum = 0
        for i in range(1,4):
            exam_points_sum += int(items[i])
        exams[items[0]] = exam_points_sum               
    for id, name in names.items():
        total_points = exercises[id]+exams[id]
        if total_points >= 0:
            grade = 0
        if total_points > 14:
            grade = 1
        if total_points > 17:
            grade = 2
        if total_points > 20:
            grade = 3  
        if total_points > 23:
            grade = 4
        if total_points > 27:
            grade = 5 
        print(f"{name} {grade}") 
  
    

