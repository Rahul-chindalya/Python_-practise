#Collect Student Information:
#Student ID 
#Student Name 
#Attendance 
#Number of subjects
#Total Score 
#Continue input

student_id= int(input("Enter student id: "))
student_name=input("Enter student name: ")
Attendance= int(input("Enter attendence: "))

total_score = 0
no_of_subj = 0

while True:
    subj_score= int(input(f"Enter subj_score {no_of_subj +1}:"))
    total_score += subj_score
    no_of_subj +=1

    Continue =input("Do you want to enter another score (yes/no)?: ")
    if Continue.lower() != "yes":
        break

Average_score = total_score / no_of_subj

if Average_score>=85:
    print("Excellent")
elif Average_score>=70 and Average_score<=84:
    print("Good")
elif Average_score>=50 and Average_score<=69:
    print( "Average")
else :
    print("Needs improvments")

if Attendance<=75:
    print("WARNING Low Attendance")
else :
    print("Attendance Satisfied")

#output
#Print out the student’s ID, name, total score, average score, performance level, and attendance with appropriate messages.
print("===========================")
print("========output=============")
print("===========================")
print(f"STUDENT ID: {student_id}")
print(f"STUDENT NAME: {student_name}")
print(f"TOTAL SCORE: {total_score}")
print(f"Average score : {Average_score }")
print(f"Attendance : {Attendance }")




