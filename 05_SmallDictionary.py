# Create a dictionary of hindi word, where it will provide the meaning in English to the user


mydict = {
    "pankha" : "fan",
    "almari" : "wardrobe",
    "thali" : "dish",
    "gadda" : "bed",
    "vastra" : "cloths",
}

print(" The word present in the dictionary are : " , mydict.keys() )
t = input("Enter the name of the Hindi word you want to search: \n")

print("The meaning of your word is : " , mydict.get(t))
