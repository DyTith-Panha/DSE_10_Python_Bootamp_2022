String = input("Enter a string: ")
String1 = String[0:len(String)//2]
String2 = String[len(String)//2:len(String)]

if String == '':
    print('The string is empty.')
else:
    print(f"{String1}{String2}")