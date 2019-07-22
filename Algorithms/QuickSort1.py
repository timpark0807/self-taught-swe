# mistake: boundary in partition should be initialized to the low value, not 0
# so that during recursive calls, the partition function sorts the correct subarray
# when boundary is intialized to 0, the partition begins at the beginning of the list.

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
            arr[boundary], arr[index] = arr[index], arr[boundary]
            boundary += 1
    arr[boundary], arr[high] = arr[high], arr[boundary]
    return boundary


arr = [10, 34, 4, 76, 5]
n = len(arr)
result = quick_sort(arr, 0, n-1)
print(result)
