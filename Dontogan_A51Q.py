print("What is your average grade")
Avggrade = int(input())
print("What is your Conduct Grade")
Conduct = int(input())
grade = input("Do you have a failing grade" )
if Avggrade >= 85:
    print("Qualified for scholarship")
else:
 print("Not Qualified: General averager is too low")
if Conduct >= 80:
    print("Qualified for scholarship")
else:
 print("Not Qualified: Conduct grade is too low")
