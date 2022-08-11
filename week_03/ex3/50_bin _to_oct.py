def BinToOct(m):
    try:
        return oct(int(m, 2))
    except ValueError:
        return'This is not a binary number'


result = BinToOct(input('yes: '))
print(result[2:])