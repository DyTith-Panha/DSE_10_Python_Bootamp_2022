def dec_to_hexa(num):
    return hex(num).replace("0x", "")


result = dec_to_hexa(int(input("please enter number from 0-15: ")))
print(result.upper())
