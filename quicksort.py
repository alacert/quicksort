import random
import math

number_list = [2, 65, 32, 53, 6, 78, 32, 24, 84, 95, 8, 3, 21]

def check_if_ordered(numbers):
    for index, value in enumerate(numbers):
        # check if last value if so break from loop
        if index+1 >= len(numbers):
            break
        if numbers[index] > numbers[index+1]:
            return False
    return True

def quicksort(item_list):
    # check if list is already ordered if so return the item list
    if check_if_ordered(item_list):
        return item_list

    # choose the pivot index randomly and get the value at that index
    pivot_index = random.randint(0, len(item_list)-1)
    pivot_value = item_list[pivot_index]

    first = []
    second = [pivot_value]

    for index, item in enumerate(item_list):
        # ignore the pivot in the for loop as its already in the list
        if index == pivot_index:
            continue
        # if smaller then the pivot add to array one, if not add to array 2
        if item < pivot_value:
            first.append(item)
        else:
            second.append(item)

    # recursively call this function until the whole list is sorted and return the value
    return quicksort(first)+ quicksort(second)

print(quicksort(number_list))
