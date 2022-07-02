String = input("Enter a string: ")
String_1 = String[0:len(String)//2]
String_2 = String[len(String)//2:len(String)]
Reverse_String = String_1[::-1]
if String == '':
    print('The string is empty.')
else:
    print(f"{Reverse_String}{String_2}")