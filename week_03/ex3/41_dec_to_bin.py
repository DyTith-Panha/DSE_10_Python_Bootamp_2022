def dec_to_bin(num):
    return bin(num).replace("0b", "")


result = dec_to_bin(int(input("please enter number from 0-9 ")))
print(result)
