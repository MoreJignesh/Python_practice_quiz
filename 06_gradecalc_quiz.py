#write a program to calculate the grade of the student from his marks

marks = int(input("Enter the marks in Maths: \n"))

if marks>95:
    print("A+")
elif marks>90:
    print("A")
elif marks>80:
    print("B+")
elif marks>70:
    print("B")
elif marks>60:
    print("C+")
elif marks>50:
    print("C")
else :
    print("Fail")