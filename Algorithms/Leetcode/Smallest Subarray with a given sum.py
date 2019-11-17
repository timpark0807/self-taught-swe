def smallest_subarray_with_given_sum(arr, s):
    """
                                r
    arr = [2, 1, 5, 2, 3, 2, 7]
                                l
           
    target = 7
    curr_sum = 0
    curr_subarray = [7]
    overall_min = [7]

    1. left, right, curr_sum, overall_min = 0, 0, 0, infinity
    1. while right < len(arr):
        - add arr[right] to current_sum,
        - increment right by 1 

        while curr_sum is greater than or equal to target
            - log current subarray
                - curr_subarr = arr[left:right]
            - check if length of current subarray is less than length overall_min subarray
                - if it is, overall_min = current_subarray
            - remove left pointer value from subarray
                - curr_sum -= arr[left]
            - increment left pointer += 1
            
    5. Return len(overall_min)

    """

    left, right = 0, 0
    curr_sum = 0
    overall_min = float('inf')

    while right < len(arr):
        curr_sum += arr[right]
        right += 1
        while curr_sum >= s:
            curr_subarray = arr[left:right]
            overall_min = min(overall_min, len(curr_subarray))
            curr_sum -= arr[left]
            left += 1

    return overall_min


print(smallest_subarray_with_given_sum([2, 1, 5, 2, 3, 2], 7))
print(smallest_subarray_with_given_sum([2, 1, 5, 2, 3, 2, 7], 7))
