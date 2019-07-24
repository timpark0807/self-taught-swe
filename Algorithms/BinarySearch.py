def binary_search(arr, low, high, num):

    while high >= low:           # base case is when high is greater than low
                                 # this clause will trigger once we have gone through every possible mid point 
        
        mid = (low + high) // 2         # split the array in half

        if arr[mid] == num:             # if the value at the middle of the array is the num
            return mid                  # return index of mid 

        if arr[mid] < num:                   # if the value at the index mid is less than the number
                                             # we can throw away everything to the left of the mid
            return binary_search(arr, mid + 1, high, num)  # recursively call binary search with the low being 1 + mid, since we already checked arr[mid] == num
        
        else:                               # else, this means value at the mid point is greater than the number
                                            # we can throw away everything to the right of the mid
            return binary_search(arr, low, mid-1, num)      # recusively call binary search with the high being mid - 1

    else:
        return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(binary_search(arr, 0, len(arr)-1, 9))
