letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def rot13Decode(new_letters):
    new_letter1 = ''
    for i in new_letters:
        if i in letters:
            if letters.index(i)<13:
                new_letter1 += letters[letters.index(i) + 13]
            else:
                new_letter1 += letters[letters.index(i) - 13]
    # print(new_letters)
    return new_letter1
# x = input("Enter words to be encoded: ")
# print("The encoded text is: ", rot13Decode(x))
choice = int(input('Press 1 to encode \nPress 2 to decode: '))
if choice == 1:
    x = input("Enter words to be encoded: ")
    print("The encoded text is: ", rot13Decode(x), '\ndo you want to continue? Y/N')
    A = str(input('enter: '))
    if A == 'Y':
        choice = int(input('Press 1 to encode \nPress 2 to decode: '))
        if choice == 1:
            x = input("Enter words to be encoded: ")
            print("The encoded text is: ", rot13Decode(x))
        elif choice == 2:
            x = input("Enter words to be decode: ")
            print("The encoded text is: ", rot13Decode(x))
    elif A == 'N':
        print('Thank you for choosing this program')
elif choice == 2:
    x = input("Enter words to be decode: ")
    print("The decode text is: ", rot13Decode(x),'\nDo you want to continue Y/N?')
    A = str(input('enter: '))
    if A == 'Y':
        choice = int(input('Press 1 to encode \nPress 2 to decode: '))
        if choice == 1:
            x = input("Enter words to be encoded: ")
            print("The encoded text is: ", rot13Decode(x))
        elif choice == 2:
            x = input("Enter words to be decode: ")
            print("The encoded text is: ", rot13Decode(x))
    elif A == 'N':
        print('Thank you for choosing this program')