#create a mini spam detector... where the user find text as "make a lot of money" ,"buy now" ,"Subscribe this", "click this" write a program to detect this spam

text = input("Enter the text you want to insert in your video: \n")

spam = False

if ("make money"  in text) : 
    spam = True
elif ("buy now"  in text) : 
    spam = True
elif ("subscribe"  in text) : 
    spam = True
elif ("click this" in text) : 
    spam = True
else:   
    spam = False

if (spam is True) : 
    print("This is a spam")
else  : 
    print("This is not a spam")
