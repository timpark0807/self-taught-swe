def bitonic_arr_max(arr):
    left = 1
    right = len(arr) - 2
    while left <= right:
        mid = (left + right) // 2
        
        # Mid is greater than left and its right neighbors
        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            return arr[mid]

        # Mid is greater than its left neighbor
        # Mid is less than it's right neighbor
        # Peak lies to the right of mid
        elif arr[mid] > arr[mid-1] and arr[mid] < arr[mid+1]:
            left = mid + 1

        # Mid is less than its left neighbor
        # Mid is greater than it's right neighbor
        # Peak lies to the left of mid
        elif arr[mid] < arr[mid-1] and arr[mid] > arr[mid+1]:
            right = mid - 1
            
#                r
#                l 
arr = [1, 3, 8, 12, 4, 2]
#      0  1  2   3  4  5
#                m
print(bitonic_arr_max(arr))

