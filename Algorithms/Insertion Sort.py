    """
        INSERTION SORT
        Runtime: O(n^2)

        Insertion sort builds a sorted array one item at a time by iterating through each value in the array.
        The algorithm compares the value at the current iteration, to the value on its left.
        If the current value is less than its left value, we swap the values and repeat. 
        If the current value is greater than or equal to its left value, the pair is sorted and we continue our array iteration.

        An overly simplistic example of insertion sort is below..
    
            1. array = [6, 7, 4]
                - The current value is 7.
                - The left value is 6.
                - 7 is greater than 6 so the pair is already sorted.
                - We continue our iteration. 

            2. array = [6, 7, 4]
                - The current value is 4.
                - The left value is 7.
                - 4 is less than 7 so we swap these values.
                - The current value is still 4.
                - The new left value is 6.
                - 4 is less than 6 so we swap these values.

            3. array = [4, 6, 7]
                The array is sorted

        Pros:
            - Simple implementation
            - Efficient for small or nearly-sorted datasets. 
            - Inplace :  Only requires a constant amount O(1) of additional memory space
            - Online  :  Can sort a list as it receives it
            - Stable  :  Does not change relative order of elements with equal keys

        Cons:
            - Less efficient for larger datasets
            - Time complexity of O(n^2)
    """

def insertion_sort(arr):
    
    """ A simple implementation of an insertion sort algorithm. """
    
    for index in range(1, len(arr)):                            # We will loop through every number in the array, beginning at index 1.
                                                                # We begin at index 1 because we will compare index 1 to index 0.
        current_value = arr[index]                              # Assign the current value of the index that we may or may not swap.
        compare_index = index - 1                               # The index of the value that we will compare the current value to is the left of the current value

        while compare_index >= 0:                               # Stop the comparison when we reach the left most value of the array, at index 0. 
            compare_value = arr[compare_index]                  # Assign the compare value to the value of the array at the compare index to improve readability.
            if current_value < compare_value:                   # If the current value is less than the compare value
                arr[compare_index + 1] = compare_value          # Swap the value at the current index to the comparison value
                arr[compare_index] = current_value              # And the value at the compare index to the current value
                compare_index -= 1                              # Decrement the compare_index so we can continue to move leftwards in the array
            else:
                break
    return arr

def insertion_sort_shorter(arr):

    """ Improvement of the first insertion sort implementation """
    
    for index in range(1, len(arr)):
        current_value = arr[index]
        compare_index = index - 1
        
        while compare_index >= 0 and current_value < arr[compare_index]:
            arr[compare_index + 1] = arr[compare_index]
            arr[compare_index] = current_value
            compare_index -= 1
            
    return arr

insertion_sort([4,3,5,2])
insertion_sort_shorter([4,3,5,2])
