def binary_multiplication(x, y):

    bin_x = bin(x).replace("0b", "")

    bin_y = bin(y).replace("0b", "")

    m_bin = bin(x * y).replace("0b", "")

    m_dec = x * y

    print(f"binary_addtion({x},{y})")

    print("Num 1 :", bin_x)

    print("Num 2 :", bin_y)

    print("Sum (Binary) :", m_bin)

    print("Sum (Decimal) :", m_dec)


binary_multiplication(60, 50)

