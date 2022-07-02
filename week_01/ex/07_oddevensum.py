Num = input("Input a number: ")
evenSum = 0
oddSum = 0

if Num.isdigit():
    for i in range (0,int(Num)+1):
        if i % 2 == 0:
            evenSum += i
        else:
            oddSum += i
    print(f"Sum even number : {evenSum}")
    print(f"Sum odd number : {oddSum}")
else:
    print("Invalid Input")
    print("Sum odd number = 0")
    print("Sum odd number = 0")