""" Write a function - duplicate_items to find the redundant or repeated items in a list and return them in sorted order. 
This method should return a list of redundant integers in ascending sorted order (as illustrated below). 
"""

def duplicate_items(list_numbers):
    list_numbers.sort()
    b = []
    print(list_numbers)
    for i in range(1, len(list_numbers)):
        if list_numbers[i] != list_numbers[i-1]:
            pass
        else:
            b.append(list_numbers[i])
    print(b)

    
duplicate_items([1, 3, 4, 3, 9, 8, 9, 4, 2, 1])
duplicate_items([1, 5, 2, 6, 3, 1, 8, 2, 3])
