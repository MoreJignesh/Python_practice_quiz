def greet(name):
    print("Good Morning, " + name)


greet("Jignesh")


# write a program using function to find the greatest of 3 numbers

def greatest(num1, num2, num3):
    if (num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3
    
g = greatest( 15, 18 , 24)
print(g)


#write a program using function where you convert celcius to farenheit

def ferh(cel):
    return ((cel * (9/5)) + 32)

f =  ferh(0)
print(f"Farenheit temperature is {f}")


#write a code using def where you make a sum of N

def sumnn(num):
    num= num * (num+1)/2
    return num

s = sumnn(10)
print("The sum of natural number is " + str(s))



# write a code using def to print * in desc where the n=3

n=5
for i in range(5):
    print("*"* (n-i))



# write a program using def which converts inch into cm

def tocm(inch):
    inch = inch*2.54
    return inch

c = tocm(38)
print(c)



#Write a python function to remove a given word from a string and strip it at the same time.

def remove_and_trim(string,word):
     nstr = string.replace(word, "")
     return nstr.strip()

text = "     This is your fav coder, Jignesh          "

pu = remove_and_trim(text,"fav")
print(pu)


