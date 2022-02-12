# write a program that check if the last name contains less than 10 characters or not:

lname = input("Enter your Last Name :\n")
print(len(lname))

if len(lname) > 10 :
    print("Last name is too long")
else:
    print("Thank you for the Last Name")