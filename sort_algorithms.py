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

def insertion_sort(array: list):
    
    size = array.__len__()
    for i in range(1, size):
        key = array.__getitem__(i)
        j = i - 1
        while (j >= 0 and array.__getitem__(j) > key):
            array.__setitem__(j+1, array.__getitem__(j))
            j = j - 1
        array.__setitem__(j+1, key)
    
    return array

# GAP NOT INITIALIZED
def shell_sort(array: list):
    size = array.__len__()
    for gap in range(int(size/2), 0, int(gap/2)):
        for i in range(gap, size):
            temp = array.__getitem__(i)
            for j in range(i, j >= gap and array.__getitem__(j - gap) > temp, j = j - gap):
                array.__setitem__(j, array.__getitem__(j - gap))
                
            array.__setitem__(j, temp)
    
    return array
        
def merge_sort(array: list):
    if array.__len__() == 0:
        return
    
    size = array.__len__()
    
    if size > 1:
        
        mid = int(size / 2)
        left = []
        right = []
        
        for i in range(0, mid):
            left.append(array.__getitem__(i))
        for i in range(mid, size):
            right.append(array.__getitem__(i))
        merge_sort(left)
        merge_sort(right)
        
        __merge__(array, left, right)
        return array

def __merge__(array: list, left: list, right: list):
    i = 0 
    j = 0
    k = 0
    len_left = left.__len__()
    len_right = right.__len__()
    
    while(i < len_left and j < len_right):
        
        if left.__getitem__(i) < right.__getitem__(j):
            array.__setitem__(k, left.__getitem__(i))
            k = k+1
            i = i+1
        else:
            array.__setitem__(k, right.__getitem__(j))
            k = k+1
            j = j+1
            
    while(i < len_left):
        array.__setitem__(k, left.__getitem__(i))
        k = k+1
        i = i+1
        
    while(j < len_right):
        array.__setitem__(k, right.__getitem__(j))
        k = k+1
        j = j+1
        
        
def heap_sort(array: list):
    size = array.__len__()
    
    for i in range(int(size / 2 - 1), 0):
        __heapify__(array,size,i)
    
    for i in range(size-1, 0,):
        temp = array.__getitem__(0)
        array.__setitem__(0, array.__getitem__(i))
        array.__setitem__(i, temp)
        __heapify__(array, i, 0)
    
    return array

def __heapify__(array: list, n: int, i: int):
    
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and array.__getitem__(left) > array.__getitem__(largest):
        largest = left
    if right < n and array.__getitem__(right) > array.__getitem__(largest):
        largest = right
    if largest != i:
        temp = array.__getitem__(i)
        array.__setitem__(i, array.__getitem__(largest))
        array.__setitem__(largest, temp)
        __heapify__(array, n, largest)