def hex_to_dec(hex):
    try:
        return int(hex, 16)

    except ValueError:
        return "This is nota hexa-decimal number"


result = hex_to_dec(input('yes: '))
print(result)
