def message_converter(message):

    yes = []

    if message == "":
        print("The string is empty.")

    else:

        for i in message:

            asc = ord(i)
            dec_num = int(asc)
            yes = hex(dec_num).upper().replace("0X", "")

            print(yes, end="")


message_converter("Hello")