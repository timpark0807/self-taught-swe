def rightmost_binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1
    
    while low < high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            result = mid
            low = mid + 1

        elif arr[mid] > target:
            high = mid - 1

        else:
            low = mid + 1

    return result


arr = [5, 10, 15, 25, 25, 25, 25, 25, 30]
print(rightmost_binary_search(arr,25))
