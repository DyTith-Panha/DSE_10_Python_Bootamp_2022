string = str(input("Input a string: "))
if string == "":
    print("The string is empty.")
else:
    print(f"First Character:{string[0]}")
    print(f"Last character:{string[-1]}")