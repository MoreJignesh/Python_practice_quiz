#Write a program to print multiplication tables of a given number using for loop

from pickle import INT
from re import S


a = int(input("Enter your number:\n"))
for i in range(1,11):
    # print(str(a) + " x " + str(i) + " = " + str(i*a))
    print(f"{a} X {i} = {a*i}")




#write a program to greet all the person whose name is starting from 'S'

l = ["Sammy" , "Suraj" , "Nimesh", "lara", "Sandra"]

for i in l:
    if i.startswith('S'):
        print("Good Afternoon, " + i)



#Write a program to print multiplication tables of a given number using While loop

l = int(input("Enter your number:\n"))

i = 1
while i<11:
    print(f"{l} X {i} = {i*l}")
    i = i+1