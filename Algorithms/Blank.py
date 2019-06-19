# Binary search a list

def binary_search(test_list, num):
    low = 0
    high = len(test_list)-1
    mid = (high-low)//2
    
    while test_list[mid] != num:
        if test_list[mid] > num:
            high = test_list[mid]
        if test_list[mid] < num:
            low = test_list[mid]
    print(test_list[mid])





l = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
binary_search(l, 72)
