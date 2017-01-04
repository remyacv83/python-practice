def find_average(array):
    sum = 0
    nSize = len(array)
    for n in array:
     sum = sum + n

    print sum
    print nSize
    print "{:.2f}".format(sum/nSize)

find_average([5,3,6])
