#write a program where user inputs 8 numbers and only return unque list of numbers.

print("Let me return you the list of  unique numbers, even when you input repeated numbers. \nLets begin.")
t1 = int(input("Enter your 1 Number:"))
t2 = int(input("Enter your 2 Number:"))
t3 = int(input("Enter your 3 Number:"))
t4 = int(input("Enter your 4 Number:"))
t5 = int(input("Enter your 5 Number:"))
t6 = int(input("Enter your 6 Number:"))
t7 = int(input("Enter your 7 Number:"))
t8 = int(input("Enter your 8 Number:"))

mylist = {t1, t2,t3,t4,t5,t6,t7,t8}

print(mylist)


# Que : can we have a set of number "18" and str "18" as  a value in it?

s = {'18', 18}
print(s) #Answer it will work

#what will be the lenght of this program
s = set()
s.add(5)
s.add(5.0)
s.add('5')

print(s)


#This means that set can only contain either number or integer if the value is same.