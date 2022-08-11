def binarb_addition(a, b):

    bin1 = bin(int(a)).replace("0b", "")
    bin2 = bin(int(b)).replace("0b", "")

    dec1 = str(a)
    dec2 = str(b)

    sumb = []
    carry = "0"

    for i in range(len(bin1)-1, -1, -1):
        bin1 = bin1[i]
        bin2 = bin2[i]
        if bin1 == "0" and bin2 == "0" and carry == "0":
            sumb.append("0")
            carry = "0"
        elif (bin1 == "0" and bin2 == "0" and carry == "1") or (bin1 == "0" and bin2 == "1" and carry == "0") or (bin1 == "1" and bin2 == "0" and carry == "0"):
            sumb.append("1")
            carry = "0"
        elif bin1 == "1" and bin2 == "1" and carry == "0":
            sumb.append("0")
            carry = "1"
        elif bin1 == "1" and bin2 == "1" and carry == "1":
            sumb.append("1")
            carry = "1"
    if carry == "1":
        sumb.append("1")

    sumb = "".join(sumb[::-1])
    sumd = int(sumb, 2)

    print(f"binarb_addition({a},{b})")

    print("Num 1 :", bin1)

    print("Num 2 :", bin2)

    print("Sum (Binarb) :", sumb)

    print("Sum (Decimal) :", sumd)


binarb_addition(60, 50)