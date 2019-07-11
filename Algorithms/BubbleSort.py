"""
    Bubble Sort
    Runtime: O(n^2)

    Bubble sort takes multiple passes through a list and compares adjacent elements and swaps them if they are out of order.
    It continues this comparison and swap until it reaches the end of the data set.
    It then starts again with the first two elements, repeating until no swaps have occured. 
    Larger elements get pushed towards the right of the array.

    Example:
        Key
        (x) = Current Index
        |x| = Compare Index
                 
    1. First Pass
        - array = [(9), |6|, 10, 7]
        - Current index is 0, value of 9
        - Compare index is 1, value of 6
        - 9 is greater than 6, swap values
        - array = [6, (9), |10|, 7]
        - Current index is 1, value of 9
        - Compare index is 2, value of 10
        - 9 is less than 10, do not swap values
        - array = [6, 9, (10), |7|]
        - Current index is 2, value of 10
        - Compare index is 3, value of 7
        - 10 is greater than 7, swap values
        - array = [6, 9, 7, (10)]

    2. Second Pass
        - array = [(6), |9|, 7, 10]
        - Current index is 0, value of 6
        - Compare index is 1, value of 9
        - 6 is less than 9, do not swap values
        - array = [6, (9), |7|, 10]
        - Current index is 1, value of 9
        - Compare index is 2, value of 7
        - 9 is greater than 7, swap values
        - array = [6, 7, (9), |10|]
        - Current index is 2, value of 9
        - Compare index is 3, value of 10
        - 9 is less than 10, do not swap values
        - array = [6, 7, 9, (10)]

"""


def bubble_sort(arr):
    
    # Iterates the array using 2 for loops
    
    for j in range(len(arr)):                           # Traverse through all elements in the array
        
        for i in range(len(arr) - 1):                   # Compare the element at current index to element on its right
            if arr[i] > arr[i+1]:                       # If the current element is greater than the element on its right
                arr[i], arr[i+1] = arr[i+1], arr[i]     # We swap the values and continue by restarting the for loop with i = next index value
                                                        # We then compare the next index value with that elements right value
                
    return arr


bubble_sort([5, 1, 4, 8])
