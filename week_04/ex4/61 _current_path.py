import os

def current_path():

    path = os.getcwd()
    path_string = "".join(path)
    print(f"Current path of program folder:\n{path_string}")


current_path()