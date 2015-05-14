course_eval = open("Kelly.txt","w")


question1 = input("What did you like/dislike about Code Academy?")
question2 = input("What did you enjoy most about the class?")
question3 = input("How was the pace of the class? (good, too fast, too slow)")
question4 = input("What would you change about the class?")
question5 = input("Would you recommend this class to a friend? Why/why not?")

course_eval.write(question1 + "\n" + question2 + "\n" + question3 + "\n" + question4 + "\n" + question5 + "\n")


course_eval.close()
