print("Hey this program return a final grade for a student basaed on certain conditions")
def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        print("your score is ", 100)
    elif exam > 75 and projects >= 5:
        print("your score is ", 90) 
    elif exam > 50 and projects >= 2:
        print("your score is ", 75)
    else:
        print("your score is ", 0)

exam1 = int(input("chose a score from 0 to 100 "))
projects1 = int(input("chose a score for projects from 0 to 15 "))
final_grade(exam1, projects1)