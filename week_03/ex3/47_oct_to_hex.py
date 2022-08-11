def OctToHex(Hex):
    try:
        return hex(int(Hex, 8))

    except ValueError:
        return " This is not an octal number "


result = OctToHex(input('yes: '))
print(result[2:].upper())
