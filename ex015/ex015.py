def findMinor(array):
    minimum = array[0]
    for elem in array:
        if(elem < minimum):
            minimum = elem
    return minimum

arraytest = [50,203,30213,40,10,49,12,3214,4,22]
minor = findMinor(arraytest)
print(f'o menor item da array é {minor}')