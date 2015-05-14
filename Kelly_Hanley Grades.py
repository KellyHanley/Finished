def student_grades(grades):
    if grades <= 100 and grades > 90:
        print ("A")
    elif grades <= 90 and grades > 80:
        print ("B")
    elif grades <= 80 and grades > 70:
        print ("C")
    elif grades <= 70 and grades > 60:
        print ("D")
    else:
        print ("F")

student_grades(76)
