num = input("Input a number: ")
aEven = 0
aOdd = 0
evenSum = 0
oddSum = 0

if num.isdigit():
    for i in range (0,int(num)+1):
        if i % 2 == 0:
            evenSum += i
            aEven += 1
        else:
            oddSum += i
            aOdd += 1
    print(f"Average of even numbers : {evenSum/aEven}")
    print(f"Average of odd numbers : {oddSum/aOdd}")
else:
    print('Invalid Input')