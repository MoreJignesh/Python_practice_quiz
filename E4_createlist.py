'''
# write a code where user can store 7 items in the list.

name = input("Enter your name : ")
print("Today we are going to store list of your Fruits. \nLet's Start, " + name)

t1 = input("Enter the name of your Fav Fruit : \n")
t2 = input("Enter the 2nd name of Fruit you like : \n")
t3 = input("Enter the 3rd name of Fruit you like : \n")
t4 = input("Enter the 4th name of Fruit you like : \n")
t5 = input("Enter the 5th name of Fruit you like : \n")
t6 = input("Enter the 6th name of Fruit you like : \n")
t7 = input("Enter the 7th name of Fruit you like : \n")

mylist = [t1,t2,t3,t4,t5,t6,t7]

print("Let print your list," +  name)
print(mylist)
'''



# Write a program to store marks of a 6 students and store them in a sorted manner. 


name = input("Enter your Class : ")
print("Today we are going to store marks of 6 students in sorted manner. \nLet's Start to note marks for " + name)

t1 = int(input("Enter marks in Math : \n"))
t2 = int(input("Enter marks in science : \n"))
t3 = int(input("Enter marks in economics : \n"))
t4 = int(input("Enter marks in social studies : \n"))
t5 = int(input("Enter marks in drawing : \n"))
t6 = int(input("Enter marks in English : \n"))

mylist = [t1,t2,t3,t4,t5,t6]

print(mylist.sort())
print(mylist)