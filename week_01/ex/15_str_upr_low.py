String = input("Enter a string: ")
String_1 = String[0:len(String)//2]
String_2 = String[len(String)//2:len(String)]

if String == '':
    print('The string is empty.')
else:
    print(f"{String_1.upper()}{String_2.lower()}")