import random

print("$ python 01_dice.py")
rollNumber = input("Welcome to this dices game!\nEnter the number of dices you want to roll:")
result = 0

if rollNumber.isnumeric():
    while True:
        if int(rollNumber) == 1:
            randomNumber = random.randint(1, 6)
            result += randomNumber
            print(f"RESULT : {result}")
            break
        elif (int(rollNumber) >= 2) and (int(rollNumber) <= 8):
            for i in range(1, int(rollNumber) + 1):
                randomNumber = random.randint(1, 6)
                print(f"Dice {i} : {randomNumber}")
                result += randomNumber
            print(f"==========")
            print(f"RESULT : {result}")
            print(f"=" * 10)
            break
        elif (int(rollNumber) <= 0) or (int(rollNumber) >= 9):
            print("USAGE: The number must be between 1 and 8")
            rollNumber = input("Enter the number of dices you want to roll")
else:
    while True:
        print("USAGE: The number must be between 1 and 8")
        rollNumberAgain = input("Enter the number of dices you want to roll")
        if rollNumberAgain.isnumeric():
            if int(rollNumberAgain) == 1:
                randomNumber = random.randint(1, 6)
                result += randomNumber
                print(f"RESULT : {result}")
                break
            elif (int(rollNumberAgain) >= 2) and (int(rollNumberAgain) <= 8):
                for i in range(1, int(rollNumberAgain) + 1):
                    randomNumber = random.randint(1, 6)
                    print(f"Dice {i} : {randomNumber}")
                    result += randomNumber
                print(f"==========")
                print(f"RESULT : {result}")
                print(f"=" * 10)
                break
            elif (int(rollNumberAgain) <= 0) or (int(rollNumberAgain) >= 9):
                print("USAGE: The number must be between 1 and 8")
                rollNumber = input("Enter the number of dices you want to roll")