def read_file(A):

    try:

        file_read = open(A, 'r')
        file_read_string = "".join(file_read)
        print(f"{file_read_string}")
        file_read.close()

    except FileNotFoundError:

        print("Invalid FILENAME")
        return ""


read_file('hello_world.txt')