
def display_header():
    print("Student Performance Evaluator")
display_header()

def get_student_info():
 input("Please enter your name: ")
get_student_info()
i1 = float(input("Please enter your assessment 1 score: "))
i2 = float(input("Please enter your assessment 2 score: "))
i3 = float(input("Please enter your assessment 3 score: "))

def evaluate_performance():
initial_s =  i1 + i2 + i3
final_s = initial_s / (i1 + i2 + i3)
if final_s >= 90:
  level = "Outstanding"
elif final_s >= 85:
     level = "very satisfactory"
elif  final_s >= 80:
     level = "satisfactory"
elif final_s >= 75:
     level = "fairly satisfactory"
elif final_s < 75:
     level = "needs improvement"
evaluate_performance()

def display_report():
 print("Student Performance Evaluator")
 print("average grade")
 print (final_s)
 print(level)
display_report()