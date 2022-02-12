#write a program to find out the student is pass or fail, if it requires total 40% and atleast 33% in each subject to pass.
# Assume 3 sub and take makes as an input.

name = input("Enter your Student Name: \n")

math = int(input("Enter the marks you obtain in Maths : \n"))
science = int(input("Enter the marks you obtain in Science : \n"))
ss = int(input("Enter the marks you obtain in SocialStudies : \n"))

totalmarks = (math + science + ss)

if math > 33:
    print("Pass in Maths")
else:
    print("Failed in Maths")
if science > 33:
    print("Pass in Science")
else:
    print("Failed in Science")
if ss> 33:
    print("Pass in SocialStudies")
else:
    print("Failed in SocialStudies")

if totalmarks>40:
    print("Pappu to pass ho gaya")
else :
    print("Better luck next time")