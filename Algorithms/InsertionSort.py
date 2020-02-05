def insertion_sort(arr):
    """
    Basic Insertion Sort
    Time  :  O(n^2)
    Space :  O(1)
    """
    for index in range(1,len(arr)):
        current_value = arr[index]
        compare_index = index-1
        while compare_index >= 0 and current_value < arr[compare_index]:
            arr[compare_index + 1] = arr[compare_index]
            arr[compare_index] = current_value
            compare_index -= 1
    return arr

