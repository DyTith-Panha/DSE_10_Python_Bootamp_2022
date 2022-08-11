def Oct_To_Dec(num):
    try:
        return int(num, 8)

    except ValueError:
        return "This is not a binary number"


result = Oct_To_Dec(input('enter 0 - 7: '))
print(result)
