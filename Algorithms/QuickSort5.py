# mistake : calling for index in arr(low, high) in the for loop
# correct : initialize a range for the index range(low, high)

# mistake : did not increment boundary in the partition loop 
# correct : boundary += 1 in order to move to the right 


def quick_sort(arr, low, high):
    
    if low < high:
        
        p = partition(arr, low, high)
        quick_sort(arr, low, p-1)
        quick_sort(arr, p+1, high)
        
    return arr


def partition(arr, low, high):
    
    boundary = low
    pivot = arr[high]

    for index in range(low, high):
        if arr[index] < pivot:
            arr[index], arr[boundary] = arr[boundary], arr[index]
            boundary += 1

    arr[boundary], arr[high] = arr[high], arr[boundary]

    return boundary

arr = [10, 1, 5, 7, 3, 2, 4, 9, 8]
print(quick_sort(arr, 0, len(arr) - 1))
