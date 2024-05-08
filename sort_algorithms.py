def selection_sort(array: list):
    size = array.__len__()
    for i in range(0,size):
        minIndex = i
        for j in range(i+1, size):
            if array.__getitem__(minIndex) > array.__getitem__(j):     
                minIndex = j
        temp = array.__getitem__(i)
        array.__setitem__(i, array.__getitem__(minIndex))
        array.__setitem__(minIndex, temp)
    return array


def bubble_sort(array: list):
    size = array.__len__()
    for i in range(0, size-1):
        for j in range(0, size-i-1):
            if array.__getitem__(j) > array.__getitem__(j+1):
                temp = array.__getitem__(j)
                array.__setitem__(j, array.__getitem__(j+1))
                array.__setitem__(j+1, temp)
                
    return array