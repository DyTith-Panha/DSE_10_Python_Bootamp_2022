def bin_to_dec(num):
    try:
        return int(num, 2)

    except ValueError:
        return "This is not a binary number"


result = bin_to_dec(input("please enter number from 0-1: "))
print(result)
