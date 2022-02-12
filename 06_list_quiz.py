#write a code to check if the user name is present in a list

names = ["harry", "pankaj" , "nirav", "jignesh", "urusha", "dhaval"] 
name = input("Enter your name \n")

if name in names:
    print("Your name is present in the list")
else:
    print("Your name is not present in the list, thanks for checking.")