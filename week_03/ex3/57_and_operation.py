
def And_operation(a, b):
    try:

        print(f"and_operation({a, b})")

        hex_1 = a
        
        hex_2 = b

        dec_1 = int(hex_1, 16)

        dec_2 = int(hex_2, 16)

        bin_1 = bin(dec_1).replace("0b", "")

        bin_2 = bin(dec_2).replace("0b", "")

        bin_and = bin(dec_1 & dec_2)

        print(f"{bin_1} \n{bin_2} \n\n{bin_and.replace('0b','')}")

    except ValueError:

        print("This is not a hexa-decimal _ber")


And_operation("33", "3D")