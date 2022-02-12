#write a code to detect weather the text is talking about 'Harry' or not

text = input("Enter your text\n")
print(text.lower())
word = 'harry'

if word in text.lower():
    print("The text is about Harry")
else:
    print("The text is off topic")