#                       Google Interview
from time import clock

lista = sorted([1, 32 ,5 ,6, -23, 4, 1, 5, 634,31, 45, 2, 4, 6 ,7])

def pair_of_sum(data, sum=8):
    print(data)
    t1 = clock()
    lowest = 0
    highest = len(data)-1
    while (lowest < highest):
        if (data[lowest] + data[highest]) == sum:
            t2 = clock()
            total_time = t2 -t1
            print(total_time)
            return True
        elif (data[lowest] + data[highest]) < sum:
            lowest += 1
        else:
            highest -= 1
    t2 = clock()
    total_time = t2 -t1
    print(total_time)
    return False

def pair_os_sum_generator(data, sum=8):
    pass
    