from numpy import *


def matrix_multiplication(q, e):

    a1 = matrix(q)

    b2 = matrix(e)

    if a1.shape == b2.shape:

        d3 = a1 * b2

        print(f"\nMatrix 1: \n \n{a1} \n")

        print(f"Matrix 2: \n \n {b2} \n")

        print(f"The result matrix is: \n \n{d3}")

    else:

        print("Error")


matrix_multiplication('3 7 5; 2 6 7; 4 3 2', '6 5 4; 3 2 1; 1 2 3')