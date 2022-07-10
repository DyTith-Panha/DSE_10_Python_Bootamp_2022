import random
def random_tuple(numbers):
    random_numbers = random.randint(0,100)
    idk = []
    sum = 0
    for i in range(0, numbers):
        random_numbers = random.randint(0, 100)
        print(f"random number {i} : {random_numbers}")
        idk.append(random_numbers)
        sum += random_numbers
    print(tuple(idk))
    print(sum)
random_tuple(5)

