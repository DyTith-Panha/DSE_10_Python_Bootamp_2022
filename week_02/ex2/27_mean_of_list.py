def mean_of_list(yes):
    sum = 0
    for i in range(0, len(yes)):
        sum += yes[i]
        mean = sum/len(yes)
    print(mean)
mean_of_list([50,10,62,32])