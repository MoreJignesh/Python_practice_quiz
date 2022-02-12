# # write a program to find the sum of first n natural numbers

# num = int(input("Enter your number :\n"))

# sum = 1
# for i in range(1,num+1):
#     sum = (num*(num+1))/2
# print(f"The Sum of first natural number {num} is {sum}")



# # write a program to find the factorial of the given number

# num = int(input("Enter your number :\n"))

# factorial = 1
# for i in range(1, num+1):
#     factorial = factorial * i
# print(f"The factorial of {num} is {factorial}")


# #write a program to print a star pattern

# for i in range(10):
#     print("*" * (i+1))

    
#write a program to print a star pattern

n = 20
for i in range(20):
    print(" " * (n-i-1), end = "")
    print("*" * (2*i+1), end = "")
    print(" " * (n-i-1))

# PENDING QUESTIONS
# write a table of any number in reverse order
# write a code where you can print 8 at all edges 3*3