string = str(input("Enter a string: "))
new_string = ""

if string == "" :
    print("The string is empty.")
else:
    for i in range (0,len(string)):
        if string[i].islower():
            new_string += string[i].upper()
        else:
            new_string += string[i].lower()
print(new_string)