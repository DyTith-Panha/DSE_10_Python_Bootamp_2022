import datetime


def append_file(file_name):

    append = open(file_name, "a")
    choice = ""
    x = datetime.datetime.now()
    y = x.strftime("%d/%m/%y %H:%M:%S")

    while choice != "EXIT":
        choice = input(f"(type EXIT to break)$: ")

        if choice != "EXIT":
            append.write(f"[{y}] {choice} ")

        else:
            return 0


append_file("appendtext")