from random import choice, randint
from sort_algorithms import *

def get_response(user_input: list , data: list):
    lowered_list = []
    for input in user_input:
        lowered_list.append(input.lower())
    
    match(lowered_list[0]):
        case "sort":
            
            array = []
            for i in range(2, lowered_list.__len__()):
                array.append(lowered_list.__getitem__(i))
                
            match(lowered_list[1]):
                case "selection":
                    return selection_sort(array)
                case "bubble":
                    return bubble_sort(array)
                case "insertion":
                    return insertion_sort(array)
                case "shell": # not correct atm
                    return shell_sort(array)
                case "merge": # not correct atm
                    return merge_sort(array)
                case "heap": # not correct atm
                    return heap_sort(array)
                
