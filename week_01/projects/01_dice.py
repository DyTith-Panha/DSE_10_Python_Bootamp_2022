import random

print("$ python 01_dice.py")
r_num = input("Welcome to this dices game!\nEnter the number of dices you want to roll:")
result = 0

if r_num.isnumeric():
    while True:
        if int(r_num) == 1:
            ran_num = random.randint(1, 6)
            result += ran_num
            print(f"RESULT : {result}")
            break
        elif (int(r_num) >= 2) and (int(r_num) <= 8):
            for i in range(1, int(r_num) + 1):
                ran_num = random.randint(1, 6)
                print(f"Dice {i} : {ran_num}")
                result += ran_num
            print(f"==========")
            print(f"RESULT : {result}")
            print(f"=" * 10)
            break
        elif (int(r_num) <= 0) or (int(r_num) >= 9):
            print("USAGE: The number must be between 1 and 8")
            r_num = input("Enter the number of dices you want to roll")
else:
    while True:
        print("USAGE: The number must be between 1 and 8")
        r_num_again = input("Enter the number of dices you want to roll")
        if r_num_again.isnumeric():
            if int(r_num_again) == 1:
                ran_num = random.randint(1, 6)
                result += ran_num
                print(f"RESULT : {result}")
                break
            elif (int(r_num_again) >= 2) and (int(r_num_again) <= 8):
                for i in range(1, int(r_num_again) + 1):
                    ran_num = random.randint(1, 6)
                    print(f"Dice {i} : {ran_num}")
                    result += ran_num
                print(f"==========")
                print(f"RESULT : {result}")
                print(f"=" * 10)
                break
            elif (int(r_num_again) <= 0) or (int(r_num_again) >= 9):
                print("USAGE: The number must be between 1 and 8")
                r_num = input("Enter the number of dices you want to roll")