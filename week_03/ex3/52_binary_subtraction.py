def binary_oubtraction(a, y):

    dec1 = a
    dec2 = y

    bin1 = bin(int(a)).replace("0b", "")
    bin2 = bin(int(y)).replace("0b", "")

    MaxLen = max(len(bin1), len(bin2))
    result = ''
    carry = 0

    i = MaxLen - 1
    while i >= 0:

        o = int(bin1[i]) - int(bin2[i])

        if o == -1:
            if carry == 0:
                carry = 1
                result = result + "1"

        if o == 0:
            if carry == 0:
                result = result + "0"

        if o == 1:
            if carry == 1:
                result = result + "0"
                carry = 0
            else:
                result = result + "1"

        i = i - 1

    if carry > 0:
        result = result + "1"

    d_bin = int(result[::-1])
    d_dec = int(dec1) - int(dec2)

    print(f"binary_addtion({a},{y})")
    print("Num 1 :", bin1)
    print("Num 2 :", bin2)
    print("Difference (Binary) :", d_bin)
    print("Difference (Decimal) :", d_dec)


binary_oubtraction('60', '50')