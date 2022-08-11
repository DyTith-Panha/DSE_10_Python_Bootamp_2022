import os


def auto_folder(folder_names):
    path = os.path.dirname(os.path.realpath(__file__))

    if len(folder_names) > 0:

        for folders in range(len(folder_names)):

            if os.path.exists(f"{path}\{folder_names[folders]}"):

                while True:
                    choice = input(f"Are you sure you want to replace {folder_names[folders]}?[Y/N]: ")

                    if choice.upper() == "Y":
                        os.replace(f"{path}\{folder_names[folders]}", f"{path}\{folder_names[folders]}")
                        break

                    elif choice.upper() == "N":
                        break

                    else:
                        print("Invalid option")

            else:
                os.makedirs(f"{path}\{folder_names[folders]}")

        return 1

    else:
        return 0


auto_folder(["folder1", "folder2", "folder3", "folder4"])
