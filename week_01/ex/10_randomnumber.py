import random
num = int(input("Input Number : "))
sum = 0
for i in range (0,num):
    random_num = random.randint(2000, 3000)
    sum += random_num
print(f"Sum of even random numbers: {sum}")