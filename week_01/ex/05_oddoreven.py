num = input('Input a number \n: ')
x = num.isdigit()
if x == True :
    A = int(num)
    if (A % 2) == 0:
        print('The number is even')
    else:
        print('The provided number is odd')
else:
    print('Not a valid Number')
