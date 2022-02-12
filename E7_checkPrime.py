#write a program to check if the number is prime or not


num= int(input("Enter your number: \n"))

prime = True

for i in range(2,num):
    if(num%i == 0):
        prime = False
        break
        
if prime:
    print("The number is prime")
else:
    print("The number is not prime")


