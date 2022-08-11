import os


def delete_file(file_name):

    path = os.path.dirname(os.path.realpath(__file__))

    while len(file_name) > 0:

        choice = input(f"Are you sure you want to delete {file_name}? [Y/N]: ")

        if choice.upper() == "Y":

            if os.path.isdir(f"{path}\{file_name}"):
                os.rmdir(f"{path}\{file_name}")
                return 1

            if os.path.isfile(f"{path}\{file_name}"):
                os.remove(f"{path}\{file_name}")
                return 1

        elif choice.upper() == "N":
            return 0

        else:
            print("Invalid Option")

    else:
        return 0


delete_file("folder2")