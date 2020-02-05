    """
    Selection Sort

    Time  : O(n^2)
    Space : O(1)
    A sorting algorithm that divides an array into two subarrays.
    A sorted subarray at the left end, and an unsorted subarray at the right end.
    Initially, the sorted subarray is empty and the unsorted subarray is the entire list.

    The smallest element from the unsorted subarray is selected and swapped with the leftmost element in the unsorted subarray.
    The sorted subarray's boundary then moves by 1 to include the recently swapped value.
    The next smallest value in the unsorted subarray is selected and swapped with the leftmost element in the unsorted subarray.
    The sorted subarray's boundary moves by 1 again.

    Key: | = boundary
        () = Smallest
        
    1. array = [ | 20, (11), 12, 22, 64 ]
        - boundary = 0 
        - Minimum index is 1, with a value of 11
        - Swap value at minimum index with arr[boundary]
        
    2. array = [ 11, | 22, (12), 20, 64 ]
        - boundary = 1
        - Minimum index is 2, with a value of 12
        - Swap value at minimum index with arr[boundary]

    3. array = [ 11, 12, | 22, (20), 64 ]
        - boundary = 2
        - Minimum index is 3, with a value of 20
        - Swap value at minimum index with arr[boundary]

    4. array = [ 11, 12, 20, | (22), 64 ]
    5. array = [ 11, 12, 20, 22, | (64) ]
    6. array = [ 11, 12, 20, 22, 64 |   ]
    """

def selection_sort(arr):
    for i in range(len(arr)):                                   # Traverse through each element in the list
        min_index = i                                           # Set the minimum index to the first element of the unsorted list
                                                                # Find min element in remaining unsorted array
        for j in range(i+1, len(arr)):                          # in range (i+1) to end of the list
            if arr[min_index] > arr[j]:                         # if value of current minimum index is greater than value of current iteration 
                min_index = j                                   # The new minimum index is the value of the current iteration
                                                                # Once we find the minimum index,
        arr[i], arr[min_index] = arr[min_index], arr[i]         # Swap the value of the minimum index with the value of the element in the sorted array
    return arr


