def HexToOct(Oct):
    try:
        return oct(int(Oct, 16))

    except ValueError:
        return 'This is nota hexa-decimal number'


result = HexToOct(input('yes: '))
print(result[2:])
