def BinToHex(k):
    try:
        return hex(int(k, 2))
    except ValueError:
        return 'This is not a binary number'


result = BinToHex(input('yes: '))
print(result[2:].upper())
