from numpy import *


def matrix_substraction(x, y):

    x1 = matrix(x)

    x2 = matrix(y)

    x3 = x1 - x2

    print(f"\nMatrix 1: \n \n{x1} \n")

    print(f"Matrix 2: \n \n {x2} \n")

    print(f"The result matrix is: \n \n{x3}")


matrix_substraction('10 5 4 2; 5 10 9 55; 9 19 69 8; 7 8 4 5', '12 65 34 2; 1 5 8 45; 7 21 63 8; 0 78 4 65')