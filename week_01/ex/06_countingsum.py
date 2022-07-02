num = 0
while True:
    number = input("Input a number: ")
    if number == 'stop':
        break
    elif number.isdigit():
        num += int(number)
    else:
        print("The input must be a valid number")
    number = input("Input 'stop' to quit, if to continue then input a number: ")

print(f"Sum is : {num}")