import os


def current_folder():

    path = os.path.dirname(os.path.realpath(__file__))
    currentdir = os.listdir(path)

    for i in currentdir:
        check_file = os.path.isfile(i)

        if check_file:
            check1 = "File"

        else:
            check1 = "Folder"

        print(f"[{i, check1}]", end="")


current_folder()