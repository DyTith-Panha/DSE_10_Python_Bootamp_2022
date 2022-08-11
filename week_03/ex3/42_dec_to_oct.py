def dec_to_oct(num):
    return oct(num).replace("0o", "")


result = dec_to_oct(int(input("please enter number from 0-7: ")))
print(result)
