def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)

        quick_sort(arr, low, p-1)
        quick_sort(arr, p+1, high)
        
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    boundary = low

    for index in range(low, high):
        if arr[index] < pivot:
            arr[index], arr[boundary] = arr[boundary], arr[index]
            boundary += 1
    arr[boundary], arr[high] = arr[high], arr[boundary]
    
    return boundary
    
arr = [15, 1, 5, 17, 3, 24]
n = len(arr)
quick_sort(arr, 0, n-1)

